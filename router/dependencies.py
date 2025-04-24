from fastapi import APIRouter, Request, Depends
from logger.log_def import log


router = APIRouter(
    prefix="/dependencies",
    tags = ["Dependencies"],
    dependencies=[Depends(log)]
)

def convert_header(request:Request, sep : str = ":-"):
    output_header = []
    for key, value in request.headers.items():
        output_header.append(f"{key} {sep} {value}.\n")
    return output_header

@router.get("")
def get_something(sep:str = "---", headers = Depends(convert_header)):
    return {
        "Headers" : headers
    }

@router.post("")
def get_something(sep:str = "---", headers = Depends(convert_header)):
    return {
        "Headers" : headers
    }


class User:
    def __init__(self,name:str,email:str):
        self.name = name
        self.email = email

@router.get("/new")
def random(name:str,email:str,account : User = Depends(User)):
    return {
        "name" : account.name,
        "email" : account.email
    }