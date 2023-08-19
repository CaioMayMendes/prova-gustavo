from fastapi import APIRouter 

from api import usuario, endereco

api_router = APIRouter()

api_router.include_router(usuario.router, prefix="/usuario", tags=["usuario"])
api_router.include_router(endereco.router, prefix="/endereco", tags=["endereco"])
