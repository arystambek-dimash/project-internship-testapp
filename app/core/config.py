from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # FastAPI
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "My FastAPI Project"
    ALLOWED_HOSTS: List[str] = ["*"]
    DEBUG: bool = False


settings = Settings()
