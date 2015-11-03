from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.shortcuts import render
from django.http import HttpResponse

from toDoApp.models import List, Task

class UserListView(ListView):
	#template_name = "user_list.html"
	model = List

	def get_queryset(self):
		#currentUser = request.user
		#userLists = List.objects.filter(user = currentUser)
		userLists = List.objects.all()
		return userLists
		
class ListCreate(CreateView):
	model = List
	fields = ['list_title']

class TaskListView(ListView):
	#template_name = "user_list.html"
	model = Task

	def get_queryset(self):
		#currentUser = request.user
		#userLists = List.objects.filter(user = currentUser)
		listTasks = Task.objects.all()
		return listTasks

def index(request):
	#currentUser = request.user
	#lists = List.objects.filter(user = currentUser)

	return HttpResponse("welcome")


# Create your views here.

