from schemas.produto import AtualizaProduto, CriaProduto

from models.produto import Produto


class CRUDProduto():

    def cria_novo_produto(self, db, novo_produto: CriaProduto):
        produto = Produto(nome=novo_produto.nome,
                          descricao=novo_produto.descricao,
                          preco=novo_produto.preco)
        db.add(produto)
        db.commit()
        db.refresh(produto)
        return produto

    def busca_produto_por_id(self, db, id_produto: int):
        produto = db.query(Produto).filter(
            Produto.id_produto == id_produto).first()
        if not produto:
            raise Exception("Produto não encontrado")
        return produto

    def busca_produtos(self, db):
        return db.query(Produto).all()

    def remove_produto(self, db, id_produto: int):
        produto = db.query(Produto).filter(
            Produto.id_produto == id_produto).first()
        if not produto:
            raise Exception("Produto não encontrado")
        db.delete(produto)
        db.commit()

    def atualiza_produto(self, db, produto_atualizado: AtualizaProduto):
        produto = db.query(Produto).filter(
            Produto.id_produto == produto_atualizado.id_produto).first()
        if not produto:
            raise Exception("Produto não encontrado")
        if produto_atualizado.nome:
            produto.nome = produto_atualizado.nome
        if produto_atualizado.descricao:
            produto.descricao = produto_atualizado.descricao
        if produto_atualizado.preco:
            produto.preco = produto_atualizado.preco
        db.add(produto)
        db.commit()
        db.refresh(produto)
        return produto

    pass


produto = CRUDProduto()
