from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Driver
from .. import db

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('/driver-status', methods=['GET'])
@jwt_required()
def check_driver_status():
    user_id = get_jwt_identity()
    driver = Driver.query.filter_by(id=user_id).first()
    return jsonify({
        'code': 200,
        'message': '查询成功',
        'data': {
            'isDriver': driver is not None
        }
    })

@user_bp.route('/info', methods=['GET'])
@jwt_required()
def get_user_info():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404
    
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': {
            'id': user.id,
            'name': user.name,
            'phone': user.phone,
            'email': user.email
        }
    })