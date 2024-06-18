from uuid import UUID
from sqlalchemy.orm import Session

from database.models import Posts
from schemas.models import Post

def post_create(db: Session, post: Post):
    db_post = Posts(title=post.title, description=post.description)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
