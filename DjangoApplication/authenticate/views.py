from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have successfully logged in.'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In - Please Try Again...'))
            return redirect('loginPage')

    else:
        return render(request, 'login.html', {})

def logoutPage(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, use_required_attribute = False)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            messages.success(request, ('You have successfully registered.'))
            return redirect('home')

    else:
        form = SignUpForm(request.POST, use_required_attribute = False)
    
    context = {'form':form}

    return render(request, 'register.html', context)

def edit_profile(request):

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            messages.success(request, ('You have successfully updated your profile.'))
            return redirect('home')

    else:
        form = UserChangeForm(instance = request.user)
    
    context = {'form':form}


    return render(request, 'edit_profile.html', context)