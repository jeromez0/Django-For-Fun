from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def To_Do(request):
    return render(request, 'To_Do.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

