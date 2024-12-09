import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String, nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    User_from_id = Column(Integer, ForeignKey('users.id')) 
    User_to_id = Column(Integer, ForeignKey('users.id')) 
    user_from = relationship(Users)
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users) 
    url_image = Column(String(2048), nullable=False)
    created_at = Column(Integer, nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(300))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    author_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
