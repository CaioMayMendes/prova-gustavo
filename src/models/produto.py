from sqlalchemy import Column, Integer, String, Float
from database.base_class import Base


class Produto(Base):
    id_produto = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
