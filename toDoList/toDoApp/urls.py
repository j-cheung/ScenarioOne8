from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

from toDoApp.views import UserListView, createList, TaskListView, adduser, loginuser

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', login_required(UserListView.as_view()), name='list-list'),
    url(r'^createList/', views.createList, name='create-list'),
    url(r'^list/(?P<listID>[0-9]+)/$', login_required(TaskListView.as_view()), name='task-list'),
    url(r'^createTask/(?P<listID>[0-9]+)/$', views.createTask, name='create-task'),
    url(r'^adduser/', views.adduser, name='adduser'),
	url(r'^loginuser/$', views.loginuser, name='loginuser'),
	url(r'^logoutuser/', views.logoutuser, name='logoutuser'),

]