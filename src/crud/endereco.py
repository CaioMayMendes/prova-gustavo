from models.usuario import Usuario
from models.endereco import Endereco
from sqlalchemy.orm import Session

from schemas.endereco import AtualizaEndereco, CriaEndereco


class CRUDEndereco():

    def atualiza_endereco(self, db: Session, *, atualiza_endereco: AtualizaEndereco):
        endereco = db.query(Endereco).filter(
            Endereco.id_endereco == atualiza_endereco.id_endereco).first()
        if not endereco:
            raise Exception("Endereço não encontrado")

        if atualiza_endereco.descricao:
            endereco.descricao = atualiza_endereco.descricao
        if atualiza_endereco.cep:
            endereco.cep = atualiza_endereco.cep
        if atualiza_endereco.rua:
            endereco.rua = atualiza_endereco.rua
        if atualiza_endereco.complemento:
            endereco.complemento = atualiza_endereco.complemento
        if atualiza_endereco.bairro:
            endereco.bairro = atualiza_endereco.bairro
        if atualiza_endereco.cidade:
            endereco.cidade = atualiza_endereco.cidade
        if atualiza_endereco.estado:
            endereco.estado = atualiza_endereco.estado
        db.add(endereco)
        db.commit()
        return endereco

    def cria_novo_endereco(self, db: Session, *, novo_endereco: CriaEndereco):
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == novo_endereco.id_usuario).first()
        if not usuario:
            raise Exception("Usuário não encontrado")

        endereco = Endereco(usuario=usuario,
                            descricao=novo_endereco.descricao,
                            cep=novo_endereco.cep,
                            rua=novo_endereco.rua,
                            complemento=novo_endereco.complemento,
                            bairro=novo_endereco.bairro,
                            cidade=novo_endereco.cidade,
                            estado=novo_endereco.estado)
        db.add(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco

    def remove_endereco(self, db: Session, *, id_endereco: int):
        endereco = db.query(Endereco).filter(
            Endereco.id_endereco == id_endereco).first()
        if not endereco:
            raise Exception("Endereço não encontrado")
        db.delete(endereco)
        db.commit()

    def busca_endereco_por_id(self, db: Session, *, id_endereco: int):
        endereco = db.query(Endereco).filter(
            Endereco.id_endereco == id_endereco).first()
        if not endereco:
            raise Exception("Endereço não encontrado")
        return endereco

    def busca_endereco_por_id_usuario(self, db: Session, *, id_usuario: int):
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == id_usuario).first()
        if not usuario:
            raise Exception("Usuário não encontrado")

        endereco = db.query(Endereco).filter(
            Endereco.id_usuario == id_usuario).all()
        if not endereco:
            raise Exception("Não existem endereços para esse usuário")
        return endereco
    pass


endereco = CRUDEndereco()
