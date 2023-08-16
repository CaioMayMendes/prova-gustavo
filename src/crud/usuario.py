from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import CriaUsuario

class CRUDUsuario():
    def cria_novo_usuario(self, db: Session, *, novo_usuario: CriaUsuario):
        usuario = Usuario(nome=novo_usuario.nome, email=novo_usuario.email, senha=novo_usuario.senha)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    pass

usuario = CRUDUsuario()