from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.models import Post
from utils.post_crud import (
    post_create
)

router = APIRouter(tags=["posts"])


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(post: Post, db: Session = Depends(get_db)):
    return post_create(db=db, post=post)