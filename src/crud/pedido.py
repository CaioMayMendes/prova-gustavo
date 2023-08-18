from datetime import datetime
from schemas.pedido import AtualizaPedido, CriaPedido

from models.pedido import Pedido
from crud.usuario import usuario as crud_usuario
from crud.endereco import endereco as crud_endereco


class CRUDPedido():

    def cria_novo_pedido(self, db, novo_pedido: CriaPedido):
        usuario = crud_usuario.busca_usuario_por_id(
            db, id_usuario=novo_pedido.id_usuario)
        if not usuario:
            raise Exception("Usuario não encontrado")

        endereco = crud_endereco.busca_endereco_por_id(
            db, id_endereco=novo_pedido.id_endereco)
        if not endereco:
            raise Exception("Endereço não encontrado")

        if novo_pedido.status not in ['Pendente', 'Pago', 'Enviado', 'Entregue', 'Cancelado']:
            raise Exception("Status inválido")

        pedido = Pedido(id_usuario=novo_pedido.id_usuario,
                        id_endereco=novo_pedido.id_endereco,
                        status=novo_pedido.status,
                        data_pedido=datetime.now())
        db.add(pedido)
        db.commit()
        db.refresh(pedido)
        return pedido

    def busca_pedido_por_id(self, db, id_pedido: int):
        pedido = db.query(Pedido).filter(
            Pedido.id_pedido == id_pedido).first()
        if not pedido:
            raise Exception("Pedido não encontrado")
        return pedido

    def busca_pedidos(self, db):
        return db.query(Pedido).all()

    def remove_pedido(self, db, id_pedido: int):
        pedido = db.query(Pedido).filter(
            Pedido.id_pedido == id_pedido).first()
        if not pedido:
            raise Exception("Pedido não encontrado")
        db.delete(pedido)
        db.commit()

    def atualiza_pedido(self, db, pedido_atualizado: AtualizaPedido):
        pedido = db.query(Pedido).filter(
            Pedido.id_pedido == pedido_atualizado.id_pedido).first()
        if not pedido:
            raise Exception("Pedido não encontrado")

        if pedido_atualizado.id_usuario:
            usuario = crud_usuario.busca_usuario_por_id(db,
                                                        id_usuario=pedido_atualizado.id_usuario)
            if not usuario:
                raise Exception("Usuario não encontrado")
            pedido.id_usuario = pedido_atualizado.id_usuario

        if pedido_atualizado.id_endereco:
            endereco = crud_endereco.busca_endereco_por_id(db,
                                                           id_endereco=pedido_atualizado.id_endereco)
            if not endereco:
                raise Exception("Endereço não encontrado")
            pedido.id_endereco = pedido_atualizado.id_endereco

        if pedido_atualizado.status and pedido_atualizado.status not in ['Pendente', 'Pago', 'Enviado', 'Entregue', 'Cancelado']:
            raise Exception("Status inválido")
        pedido.status = pedido_atualizado.status

        db.add(pedido)
        db.commit()
        db.refresh(pedido)
        return pedido

    pass


pedido = CRUDPedido()
