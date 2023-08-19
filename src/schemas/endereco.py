import datetime
from typing import Optional

from pydantic import BaseModel

class Endereco(BaseModel):
    id_endereco: Optional[int]
    id_usario: Optional[int]
    descricao: Optional[str]
    cep: Optional[str]
    rua: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    estado: Optional[str]

class CriaEndereco(BaseModel):
    id_usario: int
    descricao: str
    cep: str
    rua: str
    complemento: str
    bairro: str
    cidade: str
    estado: str

class RetornaEndereco(Endereco):
    class Config:
        orm_mode = True

class AtualizaEndereco(Endereco):
    pass