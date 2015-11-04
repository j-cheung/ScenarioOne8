from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

from toDoApp.views import UserListView, createList, TaskListView, adduser, loginuser

urlpatterns = [
    url(r'^$', views.loginuser, name='index'),
    url(r'^mainList/', login_required(UserListView.as_view()), name='main-list'),
    url(r'^addList/', views.createList, name='add-list'),
    url(r'^selectList/(?P<listID>[0-9]+)/$', login_required(TaskListView.as_view()), name='task-list'),
    url(r'^createTask/(?P<listID>[0-9]+)/$', views.createTask, name='create-task'),
    url(r'^adduser/', views.adduser, name='adduser'),
	url(r'^loginuser/$', views.loginuser, name='loginuser'),
	url(r'^logoutuser/', views.logoutuser, name='logoutuser'),

]