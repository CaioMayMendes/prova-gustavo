from typing import Optional

from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: Optional[int]
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]

class CriaProduto(BaseModel):
    nome: str
    descricao: str
    preco: float

class RetornaProduto(Produto):
    class Config:
         orm_mode = True

class AtualizaProduto(Produto):
    pass