
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.endereco import CriaEndereco, RetornaEndereco
from crud.endereco import endereco as crud_endereco

router = APIRouter()


@router.post("", response_model=RetornaEndereco)
def cria_endereco(*, db: Session = Depends(get_db), novo_endereco: CriaEndereco) -> Any:
    """
    Cria um novo endereço.
    """

    endereco = crud_endereco.cria_endereco(db, novo_endereco=novo_endereco)
    if not endereco:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao criar endereço",
        )
    return endereco

@router.get("", response_model=list[RetornaEndereco])
def retorna_enderecos(db: Session = Depends(get_db)) -> Any:
    """
    Retorna todos os endereços.
    """
    return crud_endereco.retorna_enderecos(db=db)

@router.get("/id={id_endereco}", response_model=RetornaEndereco)
def retorna_endereco_by_id(id_endereco, db: Session = Depends(get_db)) -> Any:
    """
    Retorna endereço por ID.
    """
    endereco = crud_endereco.retorna_endereco_by_id(db=db, id_endereco=id_endereco)
    if not endereco:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario com ID: {id_endereco} não encontrado.",
        )
    return endereco