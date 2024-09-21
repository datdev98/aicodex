import unittest
from app import app, db
from products.models import Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product_success(self):
        response = self.app.post('/products/', json={'name': 'Test Product', 'price': 10.0, 'picture': 'http://example.com/pic.jpg'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Product', response.get_data(as_text=True))

    def test_get_product_success(self):
        with app.app_context():
            product = Product(name='Test Product', price=10.0, picture='http://example.com/pic.jpg')
            db.session.add(product)
            db.session.commit()
        response = self.app.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Product', response.get_data(as_text=True))

    def test_get_products_success(self):
        with app.app_context():
            product = Product(name='Test Product', price=10.0, picture='http://example.com/pic.jpg')
            db.session.add(product)
            db.session.commit()
        response = self.app.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Product', response.get_data(as_text=True))

    def test_update_product_success(self):
        with app.app_context():
            product = Product(name='Test Product', price=10.0, picture='http://example.com/pic.jpg')
            db.session.add(product)
            db.session.commit()
        response = self.app.put(f'/products/{product.id}/', json={'name': 'Updated Product', 'price': 20.0, 'picture': 'http://example.com/newpic.jpg'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Product', response.get_data(as_text=True))

    def test_delete_product_success(self):
        with app.app_context():
            product = Product(name='Test Product', price=10.0, picture='http://example.com/pic.jpg')
            db.session.add(product)
            db.session.commit()
        response = self.app.delete(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product deleted', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()