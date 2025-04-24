from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from db import db_article
from typing import List
import time


router = APIRouter(prefix="/article", tags=["Article"])

async def time_delay():
    time.sleep(5)


@router.post("/new_article", response_model=ArticleDisplay)
def add_new_article(article: ArticleBase, db : Session = Depends(get_db)):
    return db_article.create_article(db=db, request=article)

@router.get("/get_article/{id}", response_model=ArticleDisplay)
def get_article(id = int, db : Session = Depends(get_db)):
    return db_article.get_article(db=db, id=id)

@router.get("/all")
async def get_all_article(db : Session = Depends(get_db)):
    await time_delay()
    return db_article.get_all_article(db=db)