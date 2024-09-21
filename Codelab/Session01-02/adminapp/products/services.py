# services.py
from products.models import Product
from products.repositories import ProductRepository

class ProductService:
    @staticmethod
    def create_product(name, price, description=None, picture=None):
        product = Product(name=name, price=price, description=description, picture=picture)
        ProductRepository.add(product)
        return product

    @staticmethod
    def get_product(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def get_products():
        return ProductRepository.get_all()

    @staticmethod
    def update_product(product_id, name, price, description=None, picture=None):
        product = ProductRepository.get_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            product.description = description
            product.picture = picture
            ProductRepository.update()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_by_id(product_id)
        if product:
            ProductRepository.delete(product)
            return True
        return False