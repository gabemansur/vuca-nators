from django.test import TestCase
from ..models import User
from ..models import UserWatchlist
import json

# Create your tests here.
class TestCalls(TestCase):

    def test_login_found(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_logout_found(self):
        response = self.client.get('/logout')
        self.assertRedirects(response, '/')

    def test_register_found(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_criptonmarket_found(self):
        response = self.client.get('/criptonmarket')
        self.assertEqual(response.status_code, 200)

    def test_criptonmarket_content(self):
        response = self.client.get('/criptonmarket')
        self.assertContains(response, 'Fortune-Teller Cripton Market')

    def test_index_found(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'Fortune Teller')

    def test_watchlist_redirect(self):
        # A non-autenticated user will be redirected to login
        response = self.client.get('/watchlist')
        self.assertRedirects(response, '/login?next=/watchlist')

    def test_updatewatchlist_redirect(self):
        # A non-autenticated user will be redirected to login
        response = self.client.get('/updatewatchlist')
        self.assertRedirects(response, '/login?next=/updatewatchlist')

    def test_watchlist_found(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        UserWatchlist.objects.create(user=self.user, watchlist="BTC")
        response = self.client.get('/watchlist')
        self.assertEqual(response.status_code, 200)

    def test_updatewatchlist_found(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        UserWatchlist.objects.create(user=self.user, watchlist="test")
        params = json.dumps({"symbol": "BTC"})
        response = self.client.post('/updatewatchlist', content_type='application/json', data=params)

    """def test_price_checker(self):
        getPrice1 = getPrice("BTC")
        print(getPrice1)"""
