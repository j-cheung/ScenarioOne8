from django import forms
from toDoApp.models import List, Task
from django.contrib.auth.models import User

class newListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('list_title',)

class editListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('list_title',)

class newTaskForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(newTaskForm, self).__init__(*args, **kwargs)
		self.fields['description'].required = True

	class Meta:
		model = Task
		fields = ('task_title', 'description', )

class editTaskForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(editTaskForm, self).__init__(*args, **kwargs)
		self.fields['description'].required = True

	class Meta:
		model = Task
		fields = ('task_title', 'description', )


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
		username = forms.CharField(label = 'Username', max_length=20)
		password = forms.CharField(max_length=32, widget=forms.PasswordInput)
