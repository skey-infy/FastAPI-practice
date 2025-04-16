from db.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean




class DBUsers(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    articles = relationship("DBArticles", back_populates="user")


class DBArticles(Base):
    __tablename__ = "Articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("DBUsers", back_populates="articles")
