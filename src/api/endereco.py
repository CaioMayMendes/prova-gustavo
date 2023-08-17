
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.endereco import AtualizaEndereco, CriaEndereco, RetornoEndereco
from crud.endereco import endereco as crud_endereco

router = APIRouter()


@router.post("", response_model=RetornoEndereco)
def cria_endereco(*, db: Session = Depends(get_db), novo_endereco: CriaEndereco) -> Any:
    """
    Cria um novo Endereço.
    """
    try:
        return crud_endereco.cria_novo_endereco(db, novo_endereco=novo_endereco)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )


@router.delete("/{id_endereco}", status_code=200)
def remove_usuario(*, db: Session = Depends(get_db), id_endereco: int) -> Any:
    """
    Remove um endereco pelo id.
    """
    try:
        crud_endereco.remove_endereco(db, id_endereco=id_endereco)
        return {"message": f"Endereço com o ID = {id_endereco} deletado com sucesso."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Endereço não encontrado",
        )


@router.get("/{id_usuario}", response_model=List[RetornoEndereco])
def busca_enderecos_por_id_usuario(*, db: Session = Depends(get_db), id_usuario: int) -> Any:
    """
    Busca endereços pelo id usuário.
    """
    try:
        return crud_endereco.busca_endereco_por_id_usuario(db, id_usuario=id_usuario)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )


@router.patch("", response_model=RetornoEndereco)
def atualiza_endereco(*, db: Session = Depends(get_db), atualiza_endereco: AtualizaEndereco) -> Any:
    """
    Atualiza endereço.
    """
    try:
        return crud_endereco.atualiza_endereco(db, atualiza_endereco=atualiza_endereco)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.args[0],
        )
