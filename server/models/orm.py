# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import ForeignKey, func, create_engine, select
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import \
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR

DB_HOST = '120.55.160.237'
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'dashingo'

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    account = Column(VARCHAR(32))
    account_type = Column(CHAR(5))
    salt = Column(CHAR(32))
    pwd = Column(CHAR(32))
#
# class User_info(Base):
#     # 信息
#     __tablename__ = 'user_info'
#     id = Column(INTEGER, ForeignKey(User.id), primary_key=True)
#     auth = Column(INTEGER, default=0)
#     gender = Column(CHAR(1))
#     avatar = Column(VARCHAR(64))
#     create_time = Column(TIMESTAMP)
#
# class User_statistic(Base):
#     # 统计
#     __tablename__ = 'user_statistic'
#     id = Column(INTEGER, ForeignKey(User.id), primary_key=True)
#     route = Column(SMALLINT)
#     star = Column(SMALLINT)
#     follow = Column(SMALLINT)
#     follower = Column(SMALLINT)
#
# class User_addr(Base):
#     # 实时位置
#     __tablename__ = 'user_addr'
#     id = Column(INTEGER, ForeignKey(User.id), primary_key=True)
#     lat = Column(FLOAT)
#     lng = Column(FLOAT)
#     update_time = Column(TIMESTAMP)
#
# # class User_star(Base):
# #     # 收藏
# #     __tablename__ = 'user_star'
#
# class User_timeline(Base):
#     # 时间线
#     __tablename__ = 'User_timeline'
#     id = Column(INTEGER, primary_key=True, autoincrement=True)
#     uid = Column(INTEGER, ForeignKey(User.id))
#     fid = Column(INTEGER, ForeignKey(User.id))
#     action = Column(CHAR(5))
#     content = Column(TEXT)
#     create_time = Column(TIMESTAMP)
#
# class User_follow(Base):
#     # 关注
#     __tablename__ = 'User_follow'
#     id = Column(INTEGER, primary_key=True, autoincrement=True)
#     uid = Column(INTEGER, ForeignKey(User.id))
#     fid = Column(INTEGER, ForeignKey(User.id))
#
# class Route(Base):
#     # 旅程
#     __tablename__ = 'route'
#     id = Column(INTEGER, primary_key=True, autoincrement=True)
#     distance = Column(FLOAT)
#     avr_speed = Column(FLOAT)
#     total_time = Column(FLOAT)
#     weather = Column(JSON)
#     heat = Column(FLOAT)
#     cover = Column(VARCHAR(128))
#     title = Column(VARCHAR(32))
#     description = Column(TEXT)
#     state = Column(CHAR(5))
#     create_time = Column(TIMESTAMP)
#
# class Path(Base):
#     # 路径
#     __tablename__ = ''
#     id = Column(INTEGER, primary_key=True, autoincrement=True)
#     rid = Column(INTEGER, ForeignKey(Route.id))
#     lat = Column(FLOAT)
#     lng = Column(FLOAT)
#     create_time = Column(TIMESTAMP)
#
# class Event(Base):
#     # 事件
#     __tablename__ = 'event'
#     id = Column(INTEGER, primary_key=True, autoincrement=True)
#     content = Column(VARCHAR(250))
#     position = Column(VARCHAR(32))
#     lat = Column(FLOAT)
#     lng = Column(FLOAT)
#     pic = Column(VARCHAR(32))
#     tape = Column(VARCHAR(32))
#     create_time = Column(TIMESTAMP)

# class Route_comment(Base):
#     # 旅程评论
#     __tablename__ = 'route_comment'
#     id = Column(ForeignKey(Route.id))
#
# class Route_like(Base):
#     # 旅程点赞
#     __tablename__ = 'route_like'
#     id = Column(ForeignKey(Route.id))
#
# class Admin_feedback(Base):
#     # 意见反馈
#     __tablename__ = 'admin_feedback'
#     id = Column(INET, primary_key=True, autoincrement=True)
#
# class Admin_report(Base):
#     # 举报
#     __tablename__ = 'admin_report'
#     id = Column(INET, primary_key=True, autoincrement=True)

engine = create_engine('postgres://%s:%s@%s:5432/%s' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                       encoding='utf-8', echo=False,
                       pool_size=5, pool_recycle=-1)

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
