from django.contrib.auth.models import AbstractUser
from django.db import models

# Added for watchlist

class User(AbstractUser):
    pass

class UserWatchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    watchlist = models.TextField(blank=True)

    def __str__(self):
        return self.watchlist