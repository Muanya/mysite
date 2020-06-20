from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Contact_form(UserCreationForm):
	names = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ('names','username', 'email', 'message', 'password1', 'password2')