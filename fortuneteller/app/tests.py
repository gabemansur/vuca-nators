from django.test import TestCase
from .models import User

# Create your tests here.
class TestCalls(TestCase):
    def test_login_found(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register_found(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_user_create(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(self.user.username, 'testuser')

    def test_user_login(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.post('/login', {'username': 'testuser', 'password': '12345'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
