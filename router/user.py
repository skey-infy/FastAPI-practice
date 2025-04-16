from fastapi import APIRouter, Depends
from schemas import UserDetails, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List, Optional


router = APIRouter(
    prefix="/user",
    tags=['user']
)


# create 
@router.post("/", response_model=UserDisplay)
def create_user(request: UserDetails, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# read
@router.get("/all", response_model=List[UserDisplay])
def read_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

@router.get("/{id}", response_model=Optional[UserDisplay])
def read_user(id:int,db : Session = Depends(get_db)):
    return db_user.get_user(id=id,db=db)

# update
@router.put("/update_username/{id}", response_model=UserDisplay)
def update_username(id:int,user_name:str, db: Session = Depends(get_db)):
    return db_user.update_username(user_id=id, new_name=user_name, db=db)

@router.put("/update_email/{id}", response_model=UserDisplay)
def update_username(id:int,email:str, db: Session = Depends(get_db)):
    return db_user.update_email(user_id=id, new_email=email, db=db)

@router.put("/update_password/{id}", response_model=UserDisplay)
def update_username(id:int,password:str, db: Session = Depends(get_db)):
    return db_user.update_password(user_id=id, new_password=password, db=db)




# delete
@router.delete("/delete/{id}")
def delete_user(id:int, db:Session = Depends(get_db)):
    return db_user.delete_user(id, db)