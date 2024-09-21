from flask import Blueprint, request, jsonify
from users.service import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([UserService.serialize_user(user) for user in users])

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(UserService.serialize_user(user)) if user else ('', 404)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['username'], data['email'])
    return jsonify(user.__dict__), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data['username'], data['email'])
    return jsonify(user.__dict__) if user else ('', 404)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserService.delete_user(user_id)
    return ('', 204) if user else ('', 404)