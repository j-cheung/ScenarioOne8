from django.conf.urls import url
from . import views
from webapp.views import adduser

urlpatterns = [
	url(r'^adduser/', views.adduser, name='adduser'),
	url(r'^loginuser/', views.loginuser, name='loginuser'),
]