from fastapi import FastAPI, Request
from router import get,post,user,articles,test_dummy,templates, dependencies
from db import models
from db.database import engin
import time

app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(articles.router)
app.include_router(test_dummy.router)
app.include_router(templates.router)
app.include_router(dependencies.router)


@app.middleware("http")
async def time_duration_middleware(request : Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response

@app.get("/")
def home():
    return {"message"  : "Hello World"}



models.Base.metadata.create_all(engin)