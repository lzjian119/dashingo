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
from geoalchemy2 import Geometry, Geography, WKTElement

from utils.tool import md5, random_str, now_datetime

DB_HOST = '120.55.160.237'
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'dashingo'

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 手机号
    phone = Column(VARCHAR(32), unique=True)
    # 加密盐
    salt = Column(CHAR(32))
    # 密码
    pwd = Column(CHAR(32))

    def __init__(self, phone=None, pwd=None):
        self.phone = phone
        self.salt = random_str(32)
        self.pwd = md5(pwd + self.salt)

    def __repr__(self):
        return '<User %r>' % self.phone


class UserInfo(Base):
    # 信息
    __tablename__ = 'user_info'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER, unique=True, nullable=False)
    # 昵称
    nickname = Column(VARCHAR(32))
    # 权限
    auth = Column(INTEGER, default=0)
    # 性别, F/M/N - 女/男/未知
    gender = Column(CHAR(1))
    # 头像URL
    avatar = Column(VARCHAR(128))
    # 出生日期
    birth = Column(DATE)
    # 身高
    height = Column(SMALLINT)
    # 体重
    weight = Column(SMALLINT)
    # 注册时间
    register_time = Column(TIMESTAMP, default=now_datetime())

    def __repr__(self):
        return '<UserInfo %r>' % self.nickname


class UserStatistic(Base):
    # 统计数据
    __tablename__ = 'user_statistic'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER, unique=True, nullable=False)
    # 旅程次数
    route_num = Column(SMALLINT, default=0)
    # 收藏个数
    star_num = Column(SMALLINT, default=0)
    # 关注人数
    follow_num = Column(SMALLINT, default=0)
    # 粉丝人数
    follower_num = Column(SMALLINT, default=0)

    def __init__(self, uid=None):
        self.uid = uid

    def __repr__(self):
        return '<UserStatistic %r>' % self.uid


class UserAddr(Base):
    # 实时位置
    __tablename__ = 'user_addr'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER, unique=True, nullable=False)
    # 经度
    lat = Column(FLOAT, default=0)
    # 纬度
    lng = Column(FLOAT, default=0)
    # 地理位置
    pos = Column(Geography(geometry_type='POINT', srid=4326),
                 default=WKTElement('POINT(0 0)', srid=4326))
    # 更新时间
    update_time = Column(TIMESTAMP, default=now_datetime())

    def __init__(self, uid=None):
        self.uid = uid

    def __repr__(self):
        return '<UserAddr %r>' % self.uid


class UserStar(Base):
    # 收藏
    __tablename__ = 'user_star'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER, nullable=False)
    # 旅程id
    rid = Column(INTEGER, nullable=False)

    def __init__(self, uid, rid):
        self.uid = uid
        self.rid = rid


class UserTimeline(Base):
    # 时间线
    # 关注的用户的动作, 点赞/评论/收藏/发布
    __tablename__ = 'user_timeline'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 关注用户id
    fid = Column(INTEGER)
    # 动作
    action = Column(CHAR(5))
    # 动作对象id
    aid = Column(INTEGER)
    # 创建时间
    create_time = Column(TIMESTAMP, default=now_datetime())


class UserNotification(Base):
    # 通知消息
    __tablename__ = 'user_notification'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 相关用户id
    fid = Column(INTEGER)
    # 地点
    addr = Column(VARCHAR(32))
    # 操作时间
    operate_time = Column(TIMESTAMP)
    # 动作
    action = Column(CHAR(5))
    # 内容
    content = Column(VARCHAR(150))
    # 状态, Y/N - 已读/未读
    state = Column(CHAR(1), default='N')
    # 额外信息
    # 例如: {"img":"","content":"",}
    extra = Column(JSON)
    # 创建时间
    create_time = Column(TIMESTAMP, default=now_datetime())


class UserBlacklist(Base):
    # 黑名单
    __tablename__ = 'user_blacklist'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 拉黑用户id
    bid = Column(INTEGER)

    def __init__(self, uid, bid):
        self.uid = uid
        self.bid = bid


class UserFollow(Base):
    # 关注
    __tablename__ = 'user_follow'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 关注用户id
    fid = Column(INTEGER)

    def __init__(self, uid, fid):
        self.uid = uid
        self.fid = fid


class UserLike(Base):
    # 点赞
    __tablename__ = 'user_like'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 点赞对象id
    lid = Column(INTEGER)
    # 点赞对象类型, RO/US/CO - ROUTE/USER/COMMENT
    type = Column(CHAR(2))

    def __init__(self, uid, lid, type):
        self.uid = uid
        self.lid = lid
        self.type = type


class Route(Base):
    # 旅程
    __tablename__ = 'route'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 距离
    distance = Column(FLOAT)
    # 总时间
    total_time = Column(FLOAT)
    # 平均速度
    # avg_speed = distance / total_time
    # 天气状况
    # 例如: {"temp1":"10","temp2":"4","weather":"多云"}
    # 从外部API获取
    weather = Column(JSON)
    # 消耗热量
    calories = Column(FLOAT)
    # 封面图片URL
    cover = Column(VARCHAR(128))
    # 标题
    title = Column(VARCHAR(32))
    # 描述文字
    description = Column(VARCHAR(150))
    # 状态, N/Y/D - 未发布/已发布/删除
    state = Column(CHAR(1), default='N')
    # 收藏个数
    star_num = Column(SMALLINT)
    # 评论条数
    comment_num = Column(SMALLINT)
    # 点赞个数
    like_num = Column(SMALLINT)
    # 创建时间
    create_time = Column(TIMESTAMP, default=now_datetime())

    def __init__(self, weather):
        self.weather = weather


class Path(Base):
    # 路径
    __tablename__ = 'path'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 旅程id
    rid = Column(INTEGER)
    # 经度
    lat = Column(FLOAT)
    # 纬度
    lng = Column(FLOAT)
    # 创建日期
    create_time = Column(TIMESTAMP, default=now_datetime())

    def __init__(self, rid, lat, lng):
        self.rid = rid
        self.lat = lat
        self.lng = lng


class Event(Base):
    # 事件
    __tablename__ = 'event'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 旅程id
    rid = Column(INTEGER)
    # 文字内容
    content = Column(VARCHAR(250))
    # 地点名称
    position = Column(VARCHAR(32))
    # 经度
    lat = Column(FLOAT)
    # 纬度
    lng = Column(FLOAT)
    # 图片URL
    pic = Column(VARCHAR(32))
    # 录音URL
    tape = Column(VARCHAR(32))
    # 创建时间
    create_time = Column(TIMESTAMP, default=now_datetime())

    def __init__(self, rid, con, pos, lat, lng, pic, tape):
        self.rid = rid
        self.content = con
        self.pos = pos
        self.lat = lat
        self.lng = lng
        self.pic = pic
        self.tape = tape

    def __repr__(self):
        return '<Event %r>' % self.content


class RouteComment(Base):
    # 旅程评论
    __tablename__ = 'route_comment'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 回复用户id
    aid = Column(INTEGER)
    # 旅程id
    rid = Column(INTEGER)
    # 评论内容
    content = Column(VARCHAR(150))
    # 创建时间
    create_time = Column(TIMESTAMP, default=now_datetime)


class AdminFeedback(Base):
    # 意见反馈
    __tablename__ = 'admin_feedback'
    id = Column(INET, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 反馈内容
    content = Column(VARCHAR(150))
    # 创建时间
    create_time = Column(TIMESTAMP, default=now_datetime())

    def __init__(self, uid, content):
        self.uid = uid
        self.content = content

class AdminReport(Base):
    # 举报
    __tablename__ = 'admin_report'
    id = Column(INET, primary_key=True, autoincrement=True)
    # 用户id
    uid = Column(INTEGER)
    # 举报对象id
    rid = Column(INTEGER)
    # 举报对象类型, RO/US/CO - ROUTE/USER/COMMENT
    type = Column(CHAR(2))

    def __init__(self, uid, rid, type):
        self.uid = uid
        self.rid = rid
        self.type = type


engine = create_engine('postgres://%s:%s@%s:5432/%s' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                       encoding='utf-8', echo=False,
                       pool_size=5, pool_recycle=-1)

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
