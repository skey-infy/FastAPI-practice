from fastapi import APIRouter, Query, Path, Body, Depends
from typing import Optional, List
from db.database import get_db
from schemas import UserDetails




router = APIRouter(prefix="/post", tags=["Post"])


@router.post("/")
def new(data:UserDetails, db : str = Depends(get_db)):
    # print("CALL")
    return {
        "message" : "Creating post.",
        "data" : data,
        "db" : db
        }


#create user with all 3 type of parameter
@router.post("/par3/{place}")
def create_new_user_with_3_types_of_parameter(place : str,data : UserDetails, country: str):
    return {
        "path" : place,
        "counter from query" : country,
        "Data from post" : data
        }


@router.post("/new/{id}/comment/{t1}")
def add_new_comment(
    id: str,
    user_data : UserDetails, 
    comment_id:int = Query(
        None,
        title="Variable title - ID.",
        description="ID OF THE COMMENT-some randome description.",
        alias="COMMENT ID",
        deprecated=True
        ),
    content : str = Body("Hello How are you."),
    content2 : str = Body(...,min_length=10),
    v: Optional[List[str]] = Query(None),
    v2: Optional[List[str]] = Query(["md", "Shakib", "mondal"]),
    t1:int = Path(gt=10)
    ):
    return {
        "id" : id,
        "body" : user_data,
        "comment_id" : comment_id,
        "content" : content,
        "Content but mandetory" : content2
        }