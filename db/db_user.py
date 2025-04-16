from sqlalchemy.orm import Session
from schemas import UserDetails
from db.models import DBUsers
from db.hash import Hash 


def create_user(db: Session, request: UserDetails):
    new_user = DBUsers(
        user_name = request.name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user) #to generate id
    return new_user

def get_user(id):
    pass

def get_all_users(db: Session):
    return db.query(DBUsers).all()

def get_user(id:int,db : Session):
    return db.query(DBUsers).filter(DBUsers.id == id).first()

def update_username(new_name:str,user_id:int, db: Session):
    user = db.query(DBUsers).filter(DBUsers.id == user_id).first()
    if user:
        user.user_name = new_name
        db.commit()
        return user
    else:
        return {"Error" : "User Not found"}
    
def update_email(new_email:str,user_id:int, db: Session):
    user = db.query(DBUsers).filter(DBUsers.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        return user
    else:
        return {"Error" : "User Not found"}
    
def update_password(new_password:str,user_id:int, db: Session):
    user = db.query(DBUsers).filter(DBUsers.id == user_id).first()
    if user:
        user.password = Hash.bcrypt(new_password)
        db.commit()
        return user
    else:
        return {"Error" : "User Not found"}
    
def delete_user(user_id:int, db:Session):
    user = db.query(DBUsers).filter(DBUsers.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"Message" : "User_deleted"}
    else:
        return {"Error" : "User Not found"}