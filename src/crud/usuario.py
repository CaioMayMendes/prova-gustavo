from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import AtualizaUsuario, CriaUsuario


class CRUDUsuario():

    def busca_todos_usuarios(self, db: Session):
        return db.query(Usuario).all()

    def busca_usuario_por_id(self, db: Session, *, id_usuario: str):
        return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    def remove_usuario(self, db: Session, *, id_usuario: str):
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == id_usuario).first()
        if not usuario:
            raise Exception("Usuário não encontrado")
        db.delete(usuario)
        db.commit()

    def atualiza_usuario(self, db: Session, *, usuarioAtualizado: AtualizaUsuario):
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == usuarioAtualizado.id_usuario).first()
        if not usuario:
            raise Exception("Usuário não encontrado")

        if usuarioAtualizado.nome:
            usuario.nome = usuarioAtualizado.nome
        if usuarioAtualizado.email:
            usuario.email = usuarioAtualizado.email
        if usuarioAtualizado.senha:
            usuario.senha = usuarioAtualizado.senha

        db.add(usuario)
        db.commit()
        return usuario

    def cria_novo_usuario(self, db: Session, *, novo_usuario: CriaUsuario):
        usuario = Usuario(nome=novo_usuario.nome,
                          email=novo_usuario.email, senha=novo_usuario.senha)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    pass


usuario = CRUDUsuario()
