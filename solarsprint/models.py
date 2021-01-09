from django.db import models
from django.contrib.auth.models import User

"""
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
"""

class UserGameInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    total_games_played = models.IntegerField(default=0)
    unlocked_pr = models.BooleanField(default=True)
    unlocked_arac = models.BooleanField(default=False)
    unlocked_arth = models.BooleanField(default=False)
    unlocked_arc = models.BooleanField(default=False)
    high_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def unlock_planet(self, planet):
        if planet=='arth':
            self.unlocked_arth=True

        elif planet=='arac':
            self.unlocked_arac = True

        elif planet=='arc':
            self.unlocked_arc = True

    def new_high_score(self, score):
        self.high_score = score




