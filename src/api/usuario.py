
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.usuario import AtualizaUsuario, CriaUsuario, RetornoUsuario
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


@router.get("", response_model=List[RetornoUsuario])
def listar_usuarios(*, db: Session = Depends(get_db)) -> Any:
    """
    Lista todos os usuários.
    """

    usuario = crud_usuario.busca_todos_usuarios(db)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum usuario encontrado",
        )
    return usuario


@router.delete("/{id_usuario}", response_model=str)
def remove_usuario(*, db: Session = Depends(get_db), id_usuario: int) -> Any:
    """
    Remove um usuário pelo id.
    """
    try:
        crud_usuario.remove_usuario(db, id_usuario=id_usuario)
        return {"message": f"Usuário com o ID = {id_usuario} deletado com sucesso."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
        )


@router.get("/{id_usuario}", response_model=RetornoUsuario)
def busca_usuario_por_id(*, db: Session = Depends(get_db), id_usuario: int) -> Any:
    """
    Busca usuário pelo id.
    """
    usuario = crud_usuario.busca_usuario_por_id(db, id_usuario=id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
        )
    return usuario


@router.patch("", response_model=RetornoUsuario)
def atualiza_usuario(*, db: Session = Depends(get_db), usuarioAtualizado: AtualizaUsuario) -> Any:
    """
    Atualiza um usuário.
    """
    try:
        return crud_usuario.atualiza_usuario(db, usuarioAtualizado=usuarioAtualizado)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
        )
