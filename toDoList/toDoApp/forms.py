from django import forms
from toDoApp.models import List, Task

class newListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('list_title',)

class newTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('task_title', 'description', )