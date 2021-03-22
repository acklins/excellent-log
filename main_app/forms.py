from django import forms
from .models import Profile
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ProfilePicForm(forms.ModelForm):
    profile_pic = ImageField(label='upload picture')
    class Meta:
        model = Profile
        fields = ('profile_pic',)

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]