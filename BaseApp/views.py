from django.shortcuts import render,redirect
from .forms import itemForm
from .models import sensorImage, item

def index(request):
    items = item.objects.all()
    return render(request, 'BaseApp/index.html', {
        'items': items
    })

def add(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = itemForm()
    return render(request, 'BaseApp/add.html', {
        'form': form
    })
