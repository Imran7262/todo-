from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def lgin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pas = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=pas)
            if user is not None:
                login(request, user)
                return redirect('index')
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
            user = form.save()
            if user is not None:
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
