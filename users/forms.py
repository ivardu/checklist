from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserSignUpForm(UserCreationForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
	password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username','fullname','email']

		help_texts = {
			'email': None, 'username':None,
		}