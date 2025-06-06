import os

class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/carpooling_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '123456'