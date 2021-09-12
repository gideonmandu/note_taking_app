from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist
from http import HTTPStatus

import src.crud.notes as crud
from src.auth.jwthandler import get_current_user
from src.schemas.notes import NoteOutSchema, NoteInSchema, UpdateNote
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter(tags=["notes"], prefix="/note")

@router.post(
    "",
    response_model=NoteOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def create_note(
    note: NoteInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> NoteOutSchema:
    return await crud.create_note(note, current_user)


@router.get(
    "s",
    response_model=list[NoteOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_notes():
    return await crud.get_notes()


@router.get(
    "/{note_id}",
    response_model=NoteOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_note(note_id: int) -> NoteOutSchema:
    try:
        return await crud.get_note(note_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Note does not exist."
        )


@router.patch(
    "/{note_id}",
    dependencies=[Depends(get_current_user)],
    response_model=NoteOutSchema,
    responses={HTTPStatus.NOT_FOUND: {"model": HTTPNotFoundError}},
)
async def update_note(
    note_id :int,
    note: UpdateNote,
    current_user: UserOutSchema = Depends(get_current_user),
    
) -> NoteOutSchema:
    return await crud.update(note_id, note, current_user)


@router.delete(
    "/{note_id}",
    response_model=Status,
    responses={HTTPStatus.NOT_FOUND: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_note(
    note_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_note(note_id, current_user)
