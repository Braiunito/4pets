from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):


	class Meta:

		model = CustomUser
		fields = ('name', 'lastname', 'residence','gender','email', 'username', 'image')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('name', 'lastname', 'residence', 'password','email', 'username', 'image')