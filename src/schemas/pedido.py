from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from schemas.endereco import RetornoEndereco

from schemas.usuario import RetornoUsuario


class PedidoBase(BaseModel):
    id_pedido: Optional[int]
    usuario: Optional[RetornoUsuario]
    endereco: Optional[RetornoEndereco]
    status: Optional[str]
    data_pedido: Optional[datetime]
    pass


class CriaPedido(PedidoBase):
    id_usuario: int
    id_endereco: int
    status: str
    pass


class AtualizaPedido(BaseModel):
    id_pedido: int
    id_usuario: Optional[int]
    id_endereco: Optional[int]
    status: Optional[str]
    pass


class RetornoPedido(PedidoBase):
    class Config:
        orm_mode = True
    pass
