import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "glenigan_takehome_FS.db")
    PORT: int = int(os.getenv("PORT", 8000))

settings = Settings()
