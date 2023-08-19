import secrets

from pydantic import BaseSettings

class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "ProvaGustavo"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:%40acv@localhost:5432/prova"

    class Config:
        env_file = ".env"


settings = Settings()