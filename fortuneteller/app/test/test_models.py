from django.test import TestCase
from ..models import User, UserWatchlist

# Create your tests here.
class TestCalls(TestCase):
    def test_user_create(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(self.user.username, 'testuser')

    def test_user_update(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.username = "newname"
        self.user.save()
        user = User.objects.get(username='newname')
        self.assertEqual(user.username, 'newname')

    def test_user_login(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.post('/login', {'username': 'testuser', 'password': '12345'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_userwatchlist_create(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        UserWatchlist.objects.create(user=self.user, watchlist='BTC,ETH,DOGE')
        userlist = UserWatchlist.objects.get(user=self.user)
        self.assertEqual(userlist.watchlist, 'BTC,ETH,DOGE')

    def test_userwatchlist_save(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        userlist = UserWatchlist.objects.create(user=self.user, watchlist='')
        userlist.watchlist = 'BTC,ETH,DOGE'
        userlist.save()
        self.assertEqual(userlist.watchlist, 'BTC,ETH,DOGE')

