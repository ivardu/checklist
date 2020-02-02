from django.shortcuts import render
from django.views.generic.edit import CreateView
from users.forms import UserSignUpForm
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(CreateView):
	form_class = UserSignUpForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('login')