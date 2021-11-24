from django.test import TestCase
from app.models import User #was .models

# Create your tests here.
class TestCalls(TestCase):
    def test_user_create(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(self.user.username, 'testuser')

    def test_user_login(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.post('/login', {'username': 'testuser', 'password': '12345'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
