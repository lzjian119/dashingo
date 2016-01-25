# -*- coding: utf-8 -*-

DB_HOST = '120.55.160.237'
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'dashingo'

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

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    account = Column(VARCHAR)
    account_type = Column(CHAR(5))
    salt = Column(CHAR(32))
    pwd = Column(CHAR(32))
    child = relationship("User_info", uselist=False, back_populates="parent")

class User_info(Base):
    # 信息
    __tablename__ = 'user_info'
    id = ForeignKey(User.id)
    openid = Column(String)
    create_time = Column(TIMESTAMP)
    auth = Column(Integer, default=0)
    gender = Column(CHAR(1))
    avatar = Column(String)

class User_statistic(Base):
    # 统计
    __tablename__ = 'user_statistic'
    id = ForeignKey(User.id)
    route = Column(Integer)
    star = Column(Integer)
    follow = Column(Integer)
    follower = Column(Integer)

class User_addr(Base):
    # 实时位置
    __tablename__ = 'user_addr'
    id = ForeignKey(User.id)
    lat = Column(FLOAT)
    lng = Column(FLOAT)

class User_star(Base):
    # 收藏
    __tablename__ = 'user_star'

class User_timeline(Base):
    # 时间线
    __tablename__ = 'User_timeline'
    id = User

class User_follow(Base):
    # 关注
    __tablename__ = 'User_follow'
    id = ForeignKey(User.id)
    follow = Column(Integer)

class Route(Base):
    # 旅程
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True, autoincrement=True)
    distance = Column(FLOAT)
    avr_speed = Column(FLOAT)
    total_time = Column(FLOAT)
    weather = Column(JSON)
    heat = Column(FLOAT)
    cover = Column(String)
    title = Column(String)
    description = Column(TEXT)
    state = Column(CHAR)

class Path(Base):
    # 路径
    __tablename__ = ''

class Event(Base):
    # 事件
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(TEXT)
    position = Column
    pic = Column(TEXT)
    tape = Column(TEXT)
    create_time = Column(TIMESTAMP)

class Route_comment(Base):
    # 旅程评论
    __tablename__ = 'route_comment'
    id = Column(ForeignKey(Route.id))

class Route_like(Base):
    # 旅程点赞
    __tablename__ = 'route_like'
    id = Column(ForeignKey(Route.id))

class Admin_feedback(Base):
    # 意见反馈
    __tablename__ = 'admin_feedback'
    id = Column(INET, primary_key=True, autoincrement=True)

class Admin_report(Base):
    # 举报
    __tablename__ = 'admin_report'
    id = Column(INET, primary_key=True, autoincrement=True)


User.addresses = relationship(
        "Address", order_by=Address.id, back_populates="user")

Base = declarative_base()
engine = create_engine('postgres://%s:%s@%s:5432/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                       encoding='utf-8', echo=False,
                       pool_size=5, pool_recycle=-1)

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
