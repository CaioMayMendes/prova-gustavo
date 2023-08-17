from typing import Optional
from pydantic import BaseModel


class CategoriaBase(BaseModel):
    id_categoria: Optional[int]
    nome: Optional[str]
    pass


class CriaCategoria(CategoriaBase):
    nome: str
    pass


class AtualizaCategoria(BaseModel):
    id_categoria: int
    nome: str
    pass


class RetornoCategoria(CategoriaBase):
    class Config:
        orm_mode = True
    pass
