from sqlalchemy.orm import Session
from models.endereco import Endereco
from schemas.endereco import CriaEndereco, RetornaEndereco

class CRUDEndereco():
    def cria_novo_usuario(self, db: Session, *, novo_endereco: CriaEndereco):
        endereco = Endereco(id_usuario = novo_endereco.id_usario,
                            descricao = novo_endereco.descricao,
                            cep = novo_endereco.cep,
                            rua = novo_endereco.rua,
                            complemento = novo_endereco.complemento,
                            bairro = novo_endereco.bairro,
                            cidade = novo_endereco.cidade,
                            estado = novo_endereco.estado)
        db.add(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco
    def retorna_endereco_by_id(self, db: Session, *, id_endereco: int ):
        return db.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()
    pass

endereco = CRUDEndereco()