from django.test import SimpleTestCase
from django.urls import reverse,resolve
from app.views import login_view,logout_view,register,cripton_market

class TestUrls(SimpleTestCase):

    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_resolved(self):
            url = reverse('logout')
            self.assertEquals(resolve(url).func, logout_view)

    def test_register_url_resolved(self):
            url = reverse('register')
            self.assertEquals(resolve(url).func, register)

    def test_criptonmarket_url_resolved(self):
        url = reverse('criptonmarket')
        self.assertEquals(resolve(url).func, cripton_market)