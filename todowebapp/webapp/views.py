from forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponseRedirect('/login/')
    else:
        form = UserForm() 

    return render(request, 'webapp/createuser.html', {'form': form})

def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Successful login")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    return render(request, 'webapp/login.html', {'form': form})




