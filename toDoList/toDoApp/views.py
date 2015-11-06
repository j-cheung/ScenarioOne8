from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


from toDoApp.models import List, Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .forms import newListForm, editListForm, newTaskForm, editTaskForm, UserForm, LoginForm 

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponseRedirect('/loginuser/')
    else:
        form = UserForm() 

    return render(request, 'toDoApp/adduser.html', {'form': form})

def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/mainList/')
                #return redirect("main-list")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    return render(request, 'toDoApp/loginuser.html', {'form': form})

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/loginuser/')


class UserListView(ListView):
	model = List
	context_object_name = 'main_list'
	template_name = "toDoApp/mainlist.html"

	def get_context_data(self, **kwargs):
		context = super(UserListView, self).get_context_data(**kwargs)
		context['user'] = self.request.user
		return context

	def get_queryset(self):
		currentUser = self.request.user
		userLists = List.objects.filter(user = currentUser)
		return userLists

@login_required(login_url = '/loginuser/')
def createList(request):
	if request.method == 'POST':
		form = newListForm(request.POST)
		if form.is_valid():
			newList = form.save(commit=False)
			newList.user = request.user
			newList.save()
			return HttpResponseRedirect('/mainList/')
	else:
		form = newListForm()

	return render(request, 'toDoApp/addList.html', {'form': form})
		
@login_required(login_url = '/loginuser/')
def editList(request, listID):
	listInstance = List.objects.get(id=listID)
	if request.method == 'POST':
		form = editListForm(request.POST or None, instance = listInstance)
		if form.is_valid():
			editList = form.save()
			return HttpResponseRedirect('/mainList/')
	else:
		form = editListForm()

	return render(request, 'toDoApp/editList.html', {'form': form})
	
def deleteList(request, listID):
	listInstance = List.objects.get(id=listID)
	listInstance.delete()
	
	return HttpResponseRedirect('/mainList/')

class TaskListView(ListView):
	template_name = "toDoApp/tasklist.html"
	context_object_name = 'task_list'

	def get_context_data(self, **kwargs):
		context = super(TaskListView, self).get_context_data(**kwargs)
		if self.list.user == self.request.user:
			context['selected_list'] = self.list
			return context

	def get_queryset(self):
		self.list = get_object_or_404(List, id=self.kwargs['listID'])
		if self.list.user == self.request.user: 
			return Task.objects.filter(theList_id = self.list.id)
		else:
			return HttpResponseRedirect('/loginuser/')


@login_required
def createTask(request, listID):
	list1 = List.objects.get(id=listID)
	if request.method == 'POST':
		form = newTaskForm(request.POST)
		if form.is_valid():
			newTask = form.save(commit=False)
			newTask.theList = List.objects.get(id=listID)
			newTask.completed = False
			newTask.save()
			
			url = reverse('task-list', args = (listID,))
			return HttpResponseRedirect(url)
	else:
		#list1 = List.objects.get(id=listID)
		form = newTaskForm()
	return render(request, 'toDoApp/addTask.html', {'form': form, 'list': list1 })
	

@login_required(login_url = '/loginuser/')
def editTask(request, taskID):
	taskInstance = Task.objects.get(id=taskID)
	if request.method == 'POST':
		form = editTaskForm(request.POST or None, instance = taskInstance)
		if form.is_valid():
			editTask = form.save()
			url = reverse('task-list', args = (taskInstance.theList.id,))
			return HttpResponseRedirect(url)
	else:
		form = editTaskForm()
	return render(request, 'toDoApp/editTask.html', {'form': form, 'list': taskInstance.theList, 'task': taskInstance})
	
def deleteTask(request, taskID):
	taskInstance = Task.objects.get(id=taskID)
	listID = taskInstance.theList.id
	taskInstance.delete()
	url = reverse('task-list', args = (listID,))
	return HttpResponseRedirect(url)


# Create your views here.

