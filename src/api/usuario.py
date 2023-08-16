
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.usuario import CriaUsuario, RetornoUsuario
from crud.usuario import usuario as crud_usuario

router = APIRouter()


@router.post("", response_model=RetornoUsuario)
def cria_usuario(*, db: Session = Depends(get_db), novo_usuario: CriaUsuario) -> Any:
    """
    Cria um novo usuario.
    """

    usuario = crud_usuario.cria_novo_usuario(db, novo_usuario=novo_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao criar usuario",
        )
    return usuario
