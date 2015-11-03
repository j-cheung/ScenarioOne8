from django.conf.urls import url

from . import views

from toDoApp.views import UserListView, ListCreate

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lists/', UserListView.as_view(), name='user-list'),
    url(r'^createList/', ListCreate.as_view(), name='create-list'),
]