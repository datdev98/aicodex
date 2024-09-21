# controllers.py
from flask import Blueprint, request, jsonify
from products.services import ProductService

products_bp = Blueprint('product_bp', __name__)

@products_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = ProductService.create_product(data['name'], data['price'], data.get('description'), data.get('picture'))
    return jsonify(product), 201

@products_bp.route('/<int:product_id>/', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@products_bp.route('/', methods=['GET'])
def get_products():
    products = ProductService.get_products()
    return jsonify(products), 200

@products_bp.route('/<int:product_id>/', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = ProductService.update_product(product_id, data['name'], data['price'], data.get('description'), data.get('picture'))
    if product:
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@products_bp.route('/<int:product_id>/', methods=['DELETE'])
def delete_product(product_id):
    success = ProductService.delete_product(product_id)
    if success:
        return jsonify({'message': 'Product deleted'}), 200
    return jsonify({'error': 'Product not found'}), 404