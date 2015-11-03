from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from toDoApp.models import List, Task
from django.contrib.auth.models import User

from .forms import newListForm, newTaskForm

class UserListView(ListView):
	#template_name = "user_list.html"
	model = List

	def get_queryset(self):
		#currentUser = request.user
		currentUser = User.objects.get(username = 'test123')
		userLists = List.objects.filter(user = currentUser)
		#userLists = List.objects.all()
		return userLists

def createList(request):
	if request.method == 'POST':
		form = newListForm(request.POST)
		if form.is_valid():
			newList = form.save(commit=False)
			newListUser = User.objects.get(username = 'test123')
			newList.user = newListUser
			newList.save()
			return HttpResponseRedirect('/lists/')
	else:
		form = newListForm()

	#return HttpResponse("hi")
	return render(request, 'toDoApp/createList.html', {'form': form})
		
#class ListCreate(CreateView):
#	model = List
#	fields = ['list_title']

class TaskListView(ListView):
	template_name = "toDoApp/task_list.html"
	#model = Task

	def get_queryset(self):
		self.list = get_object_or_404(List, id=self.args[0])
		return Task.objects.filter(theList_id = self.list)
		#currentUser = request.user
		#userLists = List.objects.filter(user = currentUser)
		#listTasks = Task.objects.all()
		#return listTasks

def createTask(request, listID):
	if request.method == 'POST':
		form = newTaskForm(request.POST)
		if form.is_valid():
			newTask = form.save(commit=False)
			newTaskList = List.objects.get(id = listID)
			newTask.completed = False;
			newTask.save()
			
			return HttpResponseRedirect('/lists/')
	else:
		form = newListForm()

	#return HttpResponse("hi")
	return render(request, 'toDoApp/createList.html', {'form': form})
		

def index(request):
	#currentUser = request.user
	#lists = List.objects.filter(user = currentUser)

	return HttpResponse("welcome")


# Create your views here.

