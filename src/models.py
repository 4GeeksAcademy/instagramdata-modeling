import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Username(Base):
  __tablename__ = 'username'
  id = Column(Integer, primary_key=True)
  username = Column(String(20), nullable=False)
  name = Column(String(25), nullable=False)
  bio = Column(String(250), nullable=True)
  email = Column(String(200), nullable=False)
  password = Column(String(20), nullable=False)
  phone_number = Column(Integer, nullable=False)
  
class Story(Base):
  __tablename__ = 'story'
  id = Column(Integer, primary_key=True)
  views = Column(Integer, nullable=False)
  caption = Column(String(250), nullable=True)
  shares = Column(Integer, nullable=True)
  media_url = Column(String(80))

class Post(Base):
  __tablename__= 'post'
  id = Column(Integer, primary_key=True)
  photo_id = Column(Integer, nullable=False)
  caption = Column(String(250), nullable=True)
  likes = Column(Integer, nullable=True)
  comment = Column(String(250), nullable=True)
  shares = Column(Integer)

class Followers(Base):
  __tablename__= 'followers'
  id = Column(Integer, primary_key=True)
  name = Column(String(25), nullable=False)
  email = Column(String(200), nullable=False)
  password = Column(String(20), nullable=False)
  bio = Column(String(250))
  phone_number = Column(Integer, nullable=False)

class User(Base):
  __tablename__= 'user'
  id = Column(Integer, primary_key=True)
  username_id = Column(Integer, ForeignKey('username.id'))
  story_id = Column(Integer, ForeignKey('story.id'))
  post_id = Column(Integer, ForeignKey('post.id'))
  followers_id = Column(Integer, ForeignKey('followers.id'))


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
