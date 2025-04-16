from fastapi import FastAPI
from router import get,post,user,articles
from db import models
from db.database import engin

app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(articles.router)


@app.get("/")
def home():
    return {"message"  : "Hello World"}



models.Base.metadata.create_all(engin)