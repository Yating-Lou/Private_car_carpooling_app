from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from .. import db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')
    
    user = User.query.filter_by(phone=phone).first()
    if not user or not user.check_password(password):
        return jsonify({'code': 401, 'message': '手机号或密码错误'}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({
        'code': 200,
        'message': '登录成功',
        'data': {
            'token': access_token,
            'user': {
                'id': user.id,
                'name': user.name,
                'phone': user.phone,
                'email': user.email
            }
        }
    })

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    password = data.get('password')
    email = data.get('email', '')

    if User.query.filter_by(phone=phone).first():
        return jsonify({'code': 400, 'message': '手机号已注册'}), 400
    
    user = User(name=name, phone=phone, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'code': 200,
        'message': '注册成功',
        'data': {
            'id': user.id,
            'name': user.name,
            'phone': user.phone
        }
    })