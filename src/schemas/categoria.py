import datetime
from typing import Optional

from pydantic import BaseModel

class Categoria(BaseModel):
    id_categoria: Optional[int]
    nome: Optional[str]

class CriaCategoria(BaseModel):
    nome: str

class RetornaCategoria(Categoria):
    class Config:
        orm_mode = True

class AtualizaCategoria(Categoria):
    pass