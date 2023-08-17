from sqlalchemy import Column, Integer, String
from database.base_class import Base


class Categoria(Base):
    id_categoria = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
