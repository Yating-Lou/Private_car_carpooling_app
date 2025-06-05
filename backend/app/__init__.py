from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化数据库
    db.init_app(app)

    # 初始化 JWT
    jwt.init_app(app)
    
    # 注册蓝图
    from .routes.login import auth_bp
    from .routes.user import user_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    return app
