from django import forms
from solarsprint.models import UserGameInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
"""
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
"""
class UserGameInfoForm(forms.ModelForm):
    class Meta():
        model = UserGameInfo
        fields = ('total_games_played', 'high_score')
