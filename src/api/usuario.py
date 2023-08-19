
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.usuario import CriaUsuario, RetornaUsuarioPublico, AtualizaUsuario
from crud.usuario import usuario as crud_usuario


router = APIRouter()


@router.post("", response_model=RetornaUsuarioPublico)
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

@router.get("", response_model=list[RetornaUsuarioPublico])
def retorna_usuario(db: Session = Depends(get_db)) -> Any:
    """
    Retorna todos os usuarios.
    """
    return crud_usuario.retorna_usuarios(db=db)

@router.get("/id={id_usuario}", response_model=RetornaUsuarioPublico)
def retorna_usuario_by_id(id_usuario, db: Session = Depends(get_db)) -> Any:
    """
    Retorna usuario por ID.
    """
    usuario = crud_usuario.retorna_usuario_by_id(db=db, id_usuario=id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario com ID: {id_usuario} não encontrado.",
        )
    return usuario

@router.patch("/id={id_usuario}", response_model=RetornaUsuarioPublico)
def atualiza_usuario_by_id(id_usuario, *, db: Session = Depends(get_db), atualiza_usuario: AtualizaUsuario) -> Any:
    """
    Atualiza usuario por ID.
    """

    usuario = crud_usuario.atualiza_usuario_by_id(db, atualiza_usuario=atualiza_usuario, id_usuario=id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario com ID: {id_usuario} não encontrado.",
        )
    return usuario

@router.delete("/id={id_usuario}", status_code=200)
def deleta_usuario_by_id(id_usuario, *, db: Session = Depends(get_db)) -> Any:
    """
    Deleta usuario por ID.
    """
    usuario = crud_usuario.deleta_usuario_by_id(db, id_usuario=id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario com ID: {id_usuario} não encontrado.",
        )
    return {"message": f"Usuario com ID: {id_usuario} deletado"}