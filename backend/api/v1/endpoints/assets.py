# backend/api/v1/assets.py
from botocore.exceptions import ClientError
from config import settings
from fastapi import APIRouter, HTTPException, Response, UploadFile, File, Query
import boto3
import mimetypes
import os
import uuid

router = APIRouter()

def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

def get_content_type(filename: str) -> str:
    """Get content type based on file extension"""
    content_type, _ = mimetypes.guess_type(filename)
    
    if content_type:
        return content_type
    
    ext = os.path.splitext(filename)[1].lower()
    content_type_map = {
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.json': 'application/json'
    }
    
    return content_type_map.get(ext, 'application/octet-stream')

def is_valid_asset_path(asset_path: str) -> bool:
    """Validate asset path for security"""
    if '..' in asset_path or asset_path.startswith('/'):
        return False
    
    valid_patterns = [
        'default/',           
        'temp/',             
        'users/',            
    ]
    
    return any(asset_path.startswith(pattern) for pattern in valid_patterns)

def get_cache_control(asset_path: str) -> str:
    """Get cache control based on asset type"""
    if asset_path.startswith('default/'):
        return "public, max-age=31536000"  
    elif asset_path.startswith('temp/'):
        return "private, max-age=3600"     
    else:
        return "private, max-age=86400"    

@router.get("/{asset_path:path}")
async def get_asset(asset_path: str):
    """
    Dynamic asset serving endpoint
    
    Supported paths:
    - default/craftapp-logo (your default logo)
    - default/favicon.ico (your default favicon)
    - users/{user_id}/projects/{project_id}/assets/logo.png (user project logo)
    - users/{user_id}/projects/{project_id}/assets/favicon.ico (user project favicon)
    - temp/{temp_id}/assets/logo.png (temporary uploads)
    """
    try:
        if not is_valid_asset_path(asset_path):
            raise HTTPException(status_code=403, detail="Invalid asset path")
        
        s3_client = get_s3_client()
        
        response = s3_client.get_object(
            Bucket=settings.S3_BUCKET_NAME,
            Key=asset_path
        )
        
        content = response['Body'].read()
        
        filename = os.path.basename(asset_path)
        content_type = get_content_type(filename)
        
        cache_control = get_cache_control(asset_path)
        
        return Response(
            content=content,
            media_type=content_type,
            headers={
                "Cache-Control": cache_control,
                "Content-Disposition": f"inline; filename={filename}",
                "Access-Control-Allow-Origin": "*",  
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "*"
            }
        )
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise HTTPException(status_code=404, detail=f"Asset not found: {asset_path}")
        elif e.response['Error']['Code'] == 'AccessDenied':
            raise HTTPException(status_code=403, detail="Access denied to asset")
        else:
            raise HTTPException(status_code=500, detail=f"S3 error: {e.response['Error']['Code']}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@router.post("/upload")
async def upload_file(
   file: UploadFile = File(...),
   folder: str = Query(..., description="Feature folder name (e.g., 'profile', 'blog', 'products')"),
):
   """
   🎯 UNIVERSAL FILE UPLOAD ENDPOINT
   
   Works for ANY feature that needs file upload:
   - Blog posts: POST /v1/assets/upload?folder=blog
   - User profiles: POST /v1/assets/upload?folder=profile  
   - Products: POST /v1/assets/upload?folder=products
   - Events: POST /v1/assets/upload?folder=events
   - Whatever: POST /v1/assets/upload?folder=whatever
   """
   
   allowed_types = [
        "image/jpeg", "image/png", "image/webp", "image/gif",
        "video/mp4", "video/webm", "video/quicktime", "video/x-msvideo",
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword",
        "text/plain"
    ]
   
   if file.content_type not in allowed_types:
       raise HTTPException(
           status_code=400, 
           detail="Only images (JPEG, PNG, WebP, GIF,), PDF, Docx, and videos (MP4, MOV, AVI, WebM) are allowed"
       )
   
   file_content = await file.read()
   if len(file_content) > 50 * 1024 * 1024:
       raise HTTPException(status_code=400, detail="File too large. Max 50MB allowed")
   
   try:
       s3_client = get_s3_client()
       
       file_extension = os.path.splitext(file.filename)[1].lower()
       unique_filename = f"{uuid.uuid4()}{file_extension}"
       
       project_id = os.getenv('PROJECT_ID', 'f8bbef17-24c5-493c-b35a-640f7dc50eb2')
       project_user_id = os.getenv('PROJECT_USER_ID', '6fb867c3-1eb3-4db1-9d24-06633e6df13c')
       
       s3_path = f"users/{project_user_id}/projects/{project_id}/assets/{folder}_{unique_filename}"
       
       s3_client.put_object(
           Bucket=settings.S3_BUCKET_NAME,
           Key=s3_path,
           Body=file_content,
           ContentType=file.content_type,
           CacheControl='public, max-age=31536000'
       )
       
       public_url = f"{settings.IMAGE_PUBLIC_URL}/v1/assets/{s3_path}"
       
       return {
           "success": True,
           "message": "File uploaded successfully",
           "s3_path": s3_path,
           "public_url": public_url,
           "folder": folder
       }
       
   except ClientError as e:
       raise HTTPException(
           status_code=500, 
           detail=f"S3 upload failed: {e.response['Error']['Message']}"
       )
   except Exception as e:
       raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")

@router.get("/default/logo")
async def get_default_logo():
    """Convenience endpoint for default logo"""
    return await get_asset("default/craftapp-logo.svg")

@router.get("/default/favicon")
async def get_default_favicon():
    """Convenience endpoint for default favicon"""
    return await get_asset("default/favicon.ico")

@router.get("/health")
async def asset_health():
    """Health check for asset service"""
    try:
        s3_client = get_s3_client()
        s3_client.head_bucket(Bucket=settings.S3_BUCKET_NAME)
        return {
            "status": "healthy", 
            "bucket": settings.S3_BUCKET_NAME,
            "service": "asset-server"
        }
    except Exception as e:
        return {
            "status": "unhealthy", 
            "error": str(e),
            "service": "asset-server"
        }