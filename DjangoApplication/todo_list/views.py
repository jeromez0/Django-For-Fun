from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html', {})

def To_Do(request):
    
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():            
            form.save()
            all_items = List.objects.all        
            messages.success(request, ('Item has been added to the list!'))
            return render(request, 'To_Do.html', {'all_items': all_items})        
    
    else:
        all_items = List.objects.all
        return render(request, 'To_Do.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('To_Do')

def complete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item has been completed!'))
    return redirect('To_Do')

def incomplete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    messages.success(request, ('Item status has been changed.'))
    return redirect('To_Do')

def edit(request, list_id):

    if request.method == "POST":
        item = List.objects.get(pk = list_id)

        form = ListForm(request.POST or None, instance = item)

        if form.is_valid():            
            form.save()
            all_items = List.objects.all        
            messages.success(request, ('Item has been edited'))
            return redirect('To_Do')
    
    else:
        item = List.objects.get(pk = list_id)
        return render(request, 'edit.html', {'item': item})

def about(request):
    fullname = "Jerome Zhang"
    return render(request, 'about.html', {'name': fullname})

def contact(request):
    return render(request, 'contact.html', {})

