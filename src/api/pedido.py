
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.pedido import AtualizaPedido, CriaPedido, RetornoPedido
from crud.pedido import pedido as crud_pedido

router = APIRouter()


@router.post("", response_model=RetornoPedido)
def cria_pedido(*, db: Session = Depends(get_db), novo_pedido: CriaPedido) -> Any:
    """
    Cria um novo Pedido.
    """
    try:
        return crud_pedido.cria_novo_pedido(db, novo_pedido=novo_pedido)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )


@router.get("/{id_pedido}", response_model=RetornoPedido)
def busca_pedido_por_id(*, db: Session = Depends(get_db), id_pedido: int) -> Any:
    """
    Busca pedido pelo id.
    """
    try:
        return crud_pedido.busca_pedido_por_id(db, id_pedido=id_pedido)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.get("", response_model=List[RetornoPedido])
def busca_pedidos(*, db: Session = Depends(get_db)) -> Any:
    """
    Lista todos os pedidos
    """
    try:
        return crud_pedido.busca_pedidos(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.delete("/{id_pedido}", status_code=200)
def remove_pedido(*, db: Session = Depends(get_db), id_pedido: int) -> Any:
    """
    Remove um pedido pelo id.
    """
    try:
        crud_pedido.remove_pedido(db, id_pedido=id_pedido)
        return {"message": f"Pedido com o ID = {id_pedido} deletado com sucesso."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.patch("", response_model=RetornoPedido)
def atualiza_pedido(*, db: Session = Depends(get_db), pedido_atualizado: AtualizaPedido) -> Any:
    """
    Atualiza pedido.
    """
    try:
        return crud_pedido.atualiza_pedido(db, pedido_atualizado=pedido_atualizado)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )
