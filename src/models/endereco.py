from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.base_class import Base


class Endereco(Base):
    id_endereco = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey(
        "usuario.id_usuario", ondelete="CASCADE"))
    descricao = Column(String(255), nullable=False)
    cep = Column(String(10), nullable=False, unique=True)
    rua = Column(String(255), nullable=False)
    complemento = Column(String(255), nullable=False)
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    estado = Column(String(2), nullable=False)

    usuario = relationship("Usuario", foreign_keys=[id_usuario])
