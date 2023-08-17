from typing import Optional
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    id_produto: Optional[int]
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]
    pass


class CriaProduto(ProdutoBase):
    nome: str
    descricao: str
    preco: float
    pass


class AtualizaProduto(BaseModel):
    id_produto: int
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]
    pass


class RetornoProduto(ProdutoBase):
    class Config:
        orm_mode = True
    pass
