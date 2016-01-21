# -*- coding: utf-8 -*-

DB_HOST = '127.0.0.1'
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'dashingo'

import os

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    account = Column(String)
    account_type = Column(String)
    salt = Column(String)
    pwd = Column(String)


class User_info(Base):
    __tablename__ = 'user_info'
    id = ForeignKey(User.id)
    openid = Column(String)
    create_time = Column(Integer)

class User_addr(Base):
    __tablename__ = 'user_addr'
    id = ForeignKey(User.id)
    lat = Column(float)
    lng = Column(float)

class User_timeline(Base):
    __tablename__ = 'User_timeline'
    id = User

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Route(Base):
    __tablename__ =  'route'
    id  = Column(Integer, primary_key=True)

class User_route(Base):
    linke

class Event

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())


db_name = 'alembic_sample.sqlite'
if os.path.exists(db_name):
    os.remove(db_name)


Base = declarative_base() #create Base lei
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                   (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                 encoding='utf-8', echo=False,
                   pool_size=100, pool_recycle=10)

engine = create_engine('sqlite:///' + db_name)

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
