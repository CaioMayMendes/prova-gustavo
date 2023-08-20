
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.categoria import CriaCategoria, RetornaCategoria
from crud.categoria import categoria as crud_categoria

router = APIRouter()


@router.post("", response_model=RetornaCategoria)
def cria_categoria(*, db: Session = Depends(get_db), nova_categoria: CriaCategoria) -> Any:
    """
    Cria uma nova categoria.
    """

    categoria = crud_categoria.cria_categoria(db, nova_categoria = nova_categoria)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao criar categoria",
        )
    return categoria

@router.get("", response_model=list[RetornaCategoria])
def retorna_categorias(db: Session = Depends(get_db)) -> Any:
    """
    Retorna todos as categorias.
    """
    return crud_categoria.retorna_categorias(db=db)

@router.get("/id={id_categoria}", response_model=RetornaCategoria)
def retorna_categoria_by_id(id_categoria, db: Session = Depends(get_db)) -> Any:
    """
    Retorna categoria por ID.
    """
    categoria = crud_categoria.retorna_categoria_by_id(db=db, id_categoria=id_categoria)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID: {id_categoria} não encontrada.",
        )
    return categoria