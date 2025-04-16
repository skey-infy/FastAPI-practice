from sqlalchemy.orm.session import Session
from db.models import DBArticles
from schemas import ArticleBase
from fastapi import HTTPException, status

def create_article(db: Session, request : ArticleBase):
    new_article = DBArticles(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.user_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article) #to generate id
    return new_article

def get_article(db:Session, id:int):
    try:
        article = db.query(DBArticles).filter(DBArticles.id == id).first()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong.")
    #handle erros
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id : - {id} not found.")
    return article

