
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.produto import AtualizaProduto, CriaProduto, RetornoProduto
from crud.produto import produto as crud_produto

router = APIRouter()


@router.post("", response_model=RetornoProduto)
def cria_produto(*, db: Session = Depends(get_db), novo_produto: CriaProduto) -> Any:
    """
    Cria um novo Produto.
    """
    try:
        return crud_produto.cria_novo_produto(db, novo_produto=novo_produto)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )


@router.get("/{id_produto}", response_model=RetornoProduto)
def busca_produto_por_id(*, db: Session = Depends(get_db), id_produto: int) -> Any:
    """
    Busca Produto pelo id.
    """
    try:
        return crud_produto.busca_produto_por_id(db, id_produto=id_produto)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.get("", response_model=List[RetornoProduto])
def busca_produtos(*, db: Session = Depends(get_db)) -> Any:
    """
    Lista todos os produtos
    """
    try:
        return crud_produto.busca_produtos(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.delete("/{id_produto}", status_code=200)
def remove_produto(*, db: Session = Depends(get_db), id_produto: int) -> Any:
    """
    Remove um produto pelo id.
    """
    try:
        crud_produto.remove_produto(db, id_produto=id_produto)
        return {"message": f"Produto com o ID = {id_produto} deletado com sucesso."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.patch("", response_model=RetornoProduto)
def atualiza_categoria(*, db: Session = Depends(get_db), produto_atualizado: AtualizaProduto) -> Any:
    """
    Atualiza produto.
    """
    try:
        return crud_produto.atualiza_produto(db, produto_atualizado=produto_atualizado)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )
