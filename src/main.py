import uvicorn

from fastapi import FastAPI

from api import api_router
from core.settings import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)