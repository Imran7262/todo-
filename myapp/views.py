from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myapp.forms import formtodo
from .models import *


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        uder=request.user
        todos = todo.objects.filter(user=uder)
        form = formtodo()
        context = {
                'form': form,
                'todos': todos,
            }
        return render(request, 'index.html', context)
    else:
        return redirect('lgin')


def lgin(request):
    if request.method=='POST':
        formm = AuthenticationForm(data=request.POST)
        if formm.is_valid():
            print('hello')
            uname = formm.cleaned_data.get('username')
            pas = formm.cleaned_data.get('password')
            user = authenticate(username=uname, password=pas)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            return HttpResponse("invalid")
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            print('form is valid')
            form.save()
            # if user is not None:
            return redirect('index')
        else:
            print('invalid')
            return render(request, 'signup.html', context)
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'signup.html', context)


def add_todo(request):
    if request.user.is_authenticated:
        uder = request.user
        form = formtodo(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = uder
            todo.save()

            return redirect('/')
        else:
            return render(request, 'signup.html', context={'form': form})


def lgout(request):
    logout(request)
    return redirect('lgin')


def dlt(request, id):
    todo.objects.get(pk=id).delete()
    return redirect('/')
