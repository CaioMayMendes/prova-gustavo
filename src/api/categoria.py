
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.categoria import AtualizaCategoria, CriaCategoria, RetornoCategoria
from crud.categoria import categoria as crud_categoria

router = APIRouter()


@router.post("", response_model=RetornoCategoria)
def cria_categoria(*, db: Session = Depends(get_db), nova_categoria: CriaCategoria) -> Any:
    """
    Cria um nova Categoria.
    """
    try:
        return crud_categoria.cria_nova_categoria(db, nova_categoria=nova_categoria)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )


@router.get("/{id_categoria}", response_model=RetornoCategoria)
def busca_categoria_por_id(*, db: Session = Depends(get_db), id_categoria: int) -> Any:
    """
    Busca categoria pelo id.
    """
    try:
        return crud_categoria.busca_categoria_por_id(db, id_categoria=id_categoria)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.get("", response_model=List[RetornoCategoria])
def busca_categorias(*, db: Session = Depends(get_db)) -> Any:
    """
    Lista todas categorias
    """
    try:
        return crud_categoria.busca_categorias(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.delete("/{id_categoria}", status_code=200)
def remove_categoria(*, db: Session = Depends(get_db), id_categoria: int) -> Any:
    """
    Remove uma categoria pelo id.
    """
    try:
        crud_categoria.remove_categoria(db, id_categoria=id_categoria)
        return {"message": f"Categoria com o ID = {id_categoria} deletado com sucesso."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrado",
        )


@router.patch("", response_model=RetornoCategoria)
def atualiza_categoria(*, db: Session = Depends(get_db), atualiza_categoria: AtualizaCategoria) -> Any:
    """
    Atualiza categoria.
    """
    try:
        return crud_categoria.atualiza_categoria(db, atualiza_categoria=atualiza_categoria)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )
