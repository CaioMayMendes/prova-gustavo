from typing import Optional
from pydantic import BaseModel

from schemas.usuario import RetornoUsuario


class EnderecoBase(BaseModel):
    id_endereco: Optional[int]
    usuario: Optional[RetornoUsuario]
    descricao: Optional[str]
    cep: Optional[str]
    rua: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    estado: Optional[str]
    pass


class CriaEndereco(EnderecoBase):
    id_usuario: int
    descricao: str
    cep: str
    rua: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    pass


class AtualizaEndereco(BaseModel):
    id_endereco: int
    descricao: Optional[str]
    cep: Optional[str]
    rua: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    estado: Optional[str]
    pass


class RetornoEndereco(EnderecoBase):
    class Config:
        orm_mode = True
    pass
