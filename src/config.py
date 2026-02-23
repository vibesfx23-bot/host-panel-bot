from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/hostbot"
    REDIS_URL: str = "redis://localhost:6379"
    
    # Hosting APIs
    CPANEL_HOSTS: dict = {}
    WHMCS_API_KEY: Optional[str] = None
    
    # Security
    JWT_SECRET: str = "your-super-secret-key-change-me"
    ADMIN_USER_IDS: list[int] = [123456789]  # Your Telegram ID
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
