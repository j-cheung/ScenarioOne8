from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
		username = forms.CharField(label = 'Username', max_length=20)
		password = forms.CharField(max_length=32, widget=forms.PasswordInput)
