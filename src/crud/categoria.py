from schemas.categoria import AtualizaCategoria, CriaCategoria

from models.categoria import Categoria


class CRUDCategoria():

    def atualiza_categoria(self, db, atualiza_categoria: AtualizaCategoria):
        categoria = db.query(Categoria).filter(
            Categoria.id_categoria == atualiza_categoria.id_categoria).first()

        if not categoria:
            raise Exception("Categoria não encontrada")
        if not atualiza_categoria.nome:
            raise Exception("Nome não pode ser vazio")

        categoria.nome = atualiza_categoria.nome
        db.add(categoria)
        db.commit()
        return categoria

    def remove_categoria(self, db, id_categoria: int):
        categoria = db.query(Categoria).filter(
            Categoria.id_categoria == id_categoria).first()
        if not categoria:
            raise Exception("Categoria não encontrada")
        db.delete(categoria)
        db.commit()

    def cria_nova_categoria(self, db, nova_categoria: CriaCategoria):
        categoria = Categoria(nome=nova_categoria.nome)
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria

    def busca_categoria_por_id(self, db, id_categoria: int):
        categoria = db.query(Categoria).filter(
            Categoria.id_categoria == id_categoria).first()
        if not categoria:
            raise Exception("Categoria não encontrada")
        return categoria

    def busca_categorias(self, db):
        return db.query(Categoria).all()

    pass


categoria = CRUDCategoria()
