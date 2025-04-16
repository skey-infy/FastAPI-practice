from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from db import db_article


router = APIRouter(prefix="/article", tags=["Article"])


@router.post("/new_article", response_model=ArticleDisplay)
def add_new_article(article: ArticleBase, db : Session = Depends(get_db)):
    return db_article.create_article(db=db, request=article)

@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id = int, db : Session = Depends(get_db)):
    return db_article.get_article(db=db, id=id)