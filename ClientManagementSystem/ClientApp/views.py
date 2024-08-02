# Assuming you have already imported necessary modules and defined your forms and models

from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import ClientModel

def AddClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showurl')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)

def ShowClient(request):
    obj = ClientModel.objects.all()
    template_name = 'show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def UpdateClient(request, id):
    obj = ClientModel.objects.get (id=id)
    form = ClientForm(instance=obj)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showurl')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)

def DeleteClient(request, id):
    obj = ClientModel.objects.get (id=id)
    obj.delete()
    return redirect('showurl')
