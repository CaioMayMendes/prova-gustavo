from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database.base_class import Base


class Pedido(Base):
    id_pedido = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey(
        "usuario.id_usuario", ondelete="CASCADE"))
    id_endereco = Column(Integer, ForeignKey(
        "endereco.id_endereco", ondelete="CASCADE"))
    status = Column(String(50), nullable=False)
    data_pedido = Column(TIMESTAMP, nullable=False)

    usuario = relationship("Usuario", foreign_keys=[id_usuario])
    endereco = relationship("Endereco", foreign_keys=[id_endereco])
