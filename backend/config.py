# backend/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
from pydantic import Extra
from urllib.parse import quote_plus

class Settings(BaseSettings):
    PROJECT_NAME: str

    PORT: int

    NEXT_PUBLIC_API_URL: str
    FRONTEND_DOMAIN: str
    IMAGE_PUBLIC_URL: str

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET_NAME: str

    PROJECT_ID: str | None = None
    PROJECT_USER_ID: str | None = None

    class Config:
        env_file = ".env"
        extra = Extra.allow  

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()