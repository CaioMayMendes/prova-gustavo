from sqlalchemy.orm import Session
from models.categoria import Categoria
from schemas.categoria import CriaCategoria, AtualizaCategoria

class CRUDCategoria():
    def cria_categoria(self, db: Session, nova_categoria: CriaCategoria):
        categoria = Categoria(nome = nova_categoria.nome)
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    def retorna_categorias(self, db: Session):
        return db.query(Categoria).all()
    def retorna_categoria_by_id(self, db: Session, *, id_categoria: int ):
        return db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    def atualiza_categoria_by_id(self, db: Session, *, id_categoria:int, categoria_atualizada: AtualizaCategoria):
        categoria = db.query(Categoria).filter(Categoria.id_endereco == id_categoria).first()
        if categoria:
            categoria.nome = categoria_atualizada.nome
    pass

categoria = CRUDCategoria()