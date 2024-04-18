from django.shortcuts import render,redirect
from .forms import itemForm
from .models import sensorImage, item

def index(request,pk=0):
    if request.method == "GET":
        items = item.objects.all()
        return render(request, 'BaseApp/index.html', {
            'items': items
        })
    else:
        if pk == 0:
            form = itemForm(request.POST)
        else:
            item_obj = item.objects.get(pk=id)
            form = itemForm(request.POST,instance=item_obj)
            return redirect("add")
        if form.is_valid():
            form.save()
        return redirect("index")
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

def delete(request,pk):
    sensor = item.objects.get(pk=pk)
    sensor.delete()
    return redirect('index')

def update_item(request, pk):
    if request.method == "POST":
        item_obj = item.objects.get(pk=pk)
        form = itemForm(request.POST, instance=item_obj)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        item_obj = item.objects.get(pk=pk)
        form = itemForm(instance=item_obj)
    return render(request, 'BaseApp/update.html', {
        'form': form
    })
