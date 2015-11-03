from django.conf.urls import url

from . import views

from toDoApp.views import UserListView, createList, TaskListView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', UserListView.as_view(), name='list-list'),
    url(r'^createList/', views.createList, name='create-list'),
    url(r'^list/(?P<listID>[0-9]+)/$', TaskListView.as_view(), name='task-list'),
    url(r'^createTask/', views.createTask, name='create-task'),

]