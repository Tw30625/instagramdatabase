import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String, nullable=False)
    firs_tname = Column(String(30), unique=True, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(16), unique=True, nullable=False)

class Followers(Base):
    __tablename__ = 'followers' 
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    use_from_id = Column(Integer, ForeignKey('user_from_id'), nullable=True)
    use_to_id = Column(Integer, ForeignKey('user_to_id'), nullable=True)

class Post(Base):
    __tablename__ = "post"   
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    User_id = Column(Integer, ForeignKey(User_id), nullable=True)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    mediatype = Column(Enum)
    url = Column(String)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)
    user = relationship(User)
    user_id = Column(Interger,ForeignKey('user_id'), nullable=True)



render_er(Base, 'diagram.png')
