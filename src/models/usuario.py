from sqlalchemy import Column, Integer, String
from database.base_class import Base

class Usuario(Base):
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)