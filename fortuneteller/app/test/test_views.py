from django.test import TestCase
from app.models import User #not importing
from api.views import getPrice

# Create your tests here.
class TestCalls(TestCase):
    def test_login_found(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register_found(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_criptonmarket_found(self):
        response = self.client.get('/criptonmarket')
        self.assertEqual(response.status_code, 200)

    def test_index_found(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    """def test_price_checker(self):
        getPrice1 = getPrice("BTC")
        print(getPrice1)"""
