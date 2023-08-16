import secrets

from pydantic import BaseSettings

class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "ProvaGustavo"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:senha@localhost:5432/nome_do_banco"

    class Config:
        env_file = ".env"


settings = Settings()