import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    id_usuario: Optional[int]
    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]

class CriaUsuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class RetornoUsuario(Usuario):
    class Config:
        orm_mode = True

class RetornaUsuarioPublico(BaseModel):
    id_usuario: Optional[int]
    nome: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True

class AtualizaUsuario(Usuario):
    pass