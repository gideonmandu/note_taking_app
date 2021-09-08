from __future__ import annotations
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Notes
from src.schemas.notes import NoteOutSchema
from src.schemas.token import Status

async def get_notes():
    """Get all notes in database

    Returns:
        [type]: [description]
    """
    return await NoteOutSchema.from_queryset(Notes.all())


async def get_note(note_id) -> NoteOutSchema:
    """Get note in database

    Args:
        note_id (int): note identifier

    Returns:
        NoteOutSchema: note object
    """
    return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))


async def create_note(note, current_user) -> NoteOutSchema:
    """Add a note to the database

    Args:
        note ([type]): [description]
        current_user ([type]): [description]

    Returns:
        NoteOutSchema: note object
    """
    note_dict = note.dict(exclude_unset=True)
    note_dict["author_id"] = current_user.id
    note_obj = await Notes.create(**note_dict)
    return await NoteOutSchema.from_tortoise_orm(note_obj)


async def update_note(note_id, current_user) -> NoteOutSchema | None:
    """Update note in database

    Raises:
        HTTPException: [description]
        HTTPException: [description]

    Returns:
        NoteOutSchema: note object
    """
    error_msg = f"Note {user_id} not found."
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=error_msg)
    if db_note.author.id == current_user.id:
        await Notes.filter(id=note_id).update(**note.dict(exclude_unset=True))
        return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    raise HTTPException(status_code=403, detail="Not authorized to update.")


async def delete_note(note_id, current_user) -> Status:
    """Delete note from database

    Raises:
        HTTPException: [description]
        HTTPException: [description]
        HTTPExceptions: [description]

    Returns:
        str: success message
    """
    error_msg = f"Note {user_id} not found."
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status=404, detail=error_msg)
    if db_note.author.id == current_user.id:
        delete_count = await Notes.filter(id=note_id).delete()
        if not delete_count:
            raise HTTPException(status_code=404, detail=error_msg)
        return Status(message=f"Deleted note {note_id}.")
    raise HTTPExceptions(status_code=403, detail="Not authorized to delete.")