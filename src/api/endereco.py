
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

    endereco = crud_endereco.cria_novo_endereco(db, novo_endereco=novo_endereco)
    if not endereco:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao criar endereço",
        )
    return endereco

@router.get("/{id_endereco}", response_model=RetornaEndereco)
def retorna_usuario(id_endereco, db: Session = Depends(get_db)) -> Any:
    """
    Retorna endereco por ID.
    """
    return crud_endereco.retorna_endereco_by_id(db=db, id_endereco=id_endereco)