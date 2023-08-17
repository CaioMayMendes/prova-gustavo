from typing import Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id_usuario: Optional[int]
    nome: Optional[str]
    email: Optional[str]


class CriaUsuario(BaseModel):
    nome: str
    email: str
    senha: str


class AtualizaUsuario(BaseModel):
    id_usuario: int
    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]


class RetornoUsuario(Usuario):
    class Config:
        orm_mode = True
