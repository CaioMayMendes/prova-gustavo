from fastapi import APIRouter

from api import usuario, endereco, categoria, produto, pedido

api_router = APIRouter()

api_router.include_router(usuario.router, prefix="/usuario", tags=["usuario"])
api_router.include_router(
    endereco.router, prefix="/endereco", tags=["endereco"])
api_router.include_router(
    categoria.router, prefix="/categoria", tags=["categoria"])
api_router.include_router(produto.router, prefix="/produto", tags=["produto"])
api_router.include_router(pedido.router, prefix="/pedido", tags=["pedido"])
