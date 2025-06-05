#数据库模型
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 用户表
class User(db.Model):
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(255))


# 司机表
class Driver(db.Model):
    __tablename__ = 'DRIVER'

    driver_id = db.Column(db.Integer, primary_key=True, nullable=False)
    carnumber = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('USERS.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), nullable=False)


# 行程表
class Trip(db.Model):
    __tablename__ = 'TRIP'

    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('DRIVER.driver_id'), nullable=False)
    passenger_id = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    time = db.Column(db.DateTime, nullable=False)
    person = db.Column(db.Integer, nullable=False)
    pickup_location = db.Column(db.String(255), nullable=False)
    dropof_location = db.Column(db.String(255), nullable=False)
    money = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)