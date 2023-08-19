from sqlalchemy import Column, Integer, String
from database.base_class import Base

class Produto(Base):
    id_produto = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    decricao = Column(String(255), nullable=False)
    preco = Column(float, nullable=False)