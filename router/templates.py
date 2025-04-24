from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from fastapi.requests import Request
from logger.log_def import log


router = APIRouter(prefix="/templated", tags=["Templated"])
template = Jinja2Templates(directory="templates")


@router.get("/{id}", response_class=HTMLResponse)
def get_article_in_template(id:int,request : Request,bg:BackgroundTasks, db : Session = Depends(get_db)):
    log("test tag","test message")
    article = db_article.get_article(db=db,id=id)
    bg.add_task(log,"Article call.","All article has been fetched.")
    return template.TemplateResponse(
        "article.html",
        {
            "request" : request,
            "title" : article.title,
            'content' : article.content,
            "user_id" : article.user_id,
            "id" : article.id,
            "published" : article.published
        }
    )