from pydantic import BaseModel
from typing import List


class UserDetails(BaseModel):
    name : str
    email : str = None
    password : str = None

# article inside UserDisplay
class Article_inside_user(BaseModel):
    id : int
    title : str
    content : str
    published : bool
    class Config():   #to convert the model to this
        orm_mode = True
    

class UserDisplay(BaseModel):
    id : int
    user_name : str
    email : str
    articles : List[Article_inside_user] = []
    class Config():   #to convert the model to this
        orm_mode = True


class ArticleBase(BaseModel):
    title : str
    content  : str
    published : bool
    user_id : int

#user inside articledisplay
class User_for_article_display(BaseModel):
    id: int
    user_name : str
    class Config():   #to convert the model to this
        orm_mode = True
        
class ArticleDisplay(BaseModel):
    title : str
    content : str
    published : bool
    user : User_for_article_display = None
    class Config():   #to convert the model to this
        orm_mode = True
