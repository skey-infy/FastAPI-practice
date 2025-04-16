from fastapi import APIRouter, Response, status

from enum import Enum
from typing import Optional

router = APIRouter(prefix="/get", tags=["get"])


@router.get("/checkpar/{id}")
def check_par(id : int):
    return {"message" : f"Given id is {id}."}

class BG(str, Enum):
    small = "small"
    long = "long"

@router.get("/type/{type}")
def func(type : BG):
    return {"msg" : type}

@router.get("/check")
def check_query_param(fname:str, last_name:str = 'Mondal'):
    return {"msg" : f"Your full name is :- {fname} {last_name}."}

@router.get("/print/{isname}")
def print_name_or_place(isname,name:str = None, place: Optional[str] = None):
    if isname.lower() == "name":
        return {"msg" : f"given name is {name}."}
    else:
        return {"msg" : f"Place name :- {place}"}
    


@router.get("/check_status_code", status_code=status.HTTP_200_OK)
def check_query_param(id:int, response:Response):
    """
    Simulates the checking of a id. if id greater than 10 it will issue a 404 error.

    - **id** mandatory uery parameter.
    """
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" : f"ID : - {id} = Content Not found."}
    else:
        return {"msg" : f"ID : - {id} = Content are here."}
    

@router.get(
        "/place/{name}", 
        tags=["name", "place"],
        summary="Prints the given name.",
        description="Prints the given name of a place in Upper letter."
        )
def place_name(name:str):
    return {"msg" : f"Given place name is {name.upper()}."}


@router.get(
        "/person/{name}", 
        tags=["name","person"],
        summary="Prints the given name.",
        description="Prints the given name of a person in Upper letter.",
        response_description="Prints the given name of a person in Upper letter."
        )
def place_name(name:str):
    return {"msg" : f"Given person name is {name.upper()}."}
