from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import CriaUsuario, AtualizaUsuario

class CRUDUsuario():
    def cria_novo_usuario(self, db: Session, *, novo_usuario: CriaUsuario):
        usuario = Usuario(nome=novo_usuario.nome, email=novo_usuario.email, senha=novo_usuario.senha)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    def retorna_usuarios(self, db: Session):
        return db.query(Usuario).all()
    def retorna_usuario_by_id(self, db: Session, *, id_usuario: int ):
        return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    def atualiza_usuario_by_id(self, db: Session, *, id_usuario: int, atualiza_usuario: AtualizaUsuario):
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario:
            usuario.nome = atualiza_usuario.nome
            usuario.email = atualiza_usuario.email
            usuario.senha = atualiza_usuario.senha
            db.commit()
            db.refresh(usuario)
            return usuario
    def deleta_usuario_by_id(self, db: Session, *, id_usuario: int):
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario:
            db.delete(usuario)
            db.commit()
            return usuario
    pass

usuario = CRUDUsuario()