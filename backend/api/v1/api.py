# backend/api/v1/api.py
from fastapi import APIRouter
from api.v1.endpoints import assets

router = APIRouter()

router.include_router(assets.router, prefix="/assets", tags=["assets"])