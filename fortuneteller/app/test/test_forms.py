from django.test import TestCase
from ..models import User

# Create your tests here.
class TestCalls(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', first_name='Test', last_name='User', password='12345')

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)

    def test_user_fullname(self):
        user = User.objects.get(id=1)
        name = user.get_full_name()
        self.assertEqual(name, 'Test User')
