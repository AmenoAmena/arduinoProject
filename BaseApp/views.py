from django.shortcuts import render,redirect
from .forms import itemForm,SignupForm
from .models import sensorImage, item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Group,User



@login_required
def index(request,pk=0):
    
    if request.method == "GET":
        items = item.objects.filter(user=request.user)
        user = request.user
        return render(request,'BaseApp/index.html',{
            'items':items,
            'user':user
        })
    
    else:
        if pk == 0:
            form = itemForm(request.POST)
        else:
            item_obj = item.objects.get(pk=pk, user=request.user)
            form = itemForm(request.POST,instance=item_obj)
            return redirect("add")
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
        return redirect("index")


@login_required
def add(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('index')
    else:
        form = itemForm()
    return render(request, 'BaseApp/add.html', {
        'form': form
    })


@login_required
def delete(request, pk):
    sensor = item.objects.get(pk=pk)
    deleted_item_user = sensor.user
    if deleted_item_user == request.user:
        sensor.delete()
    return redirect('index')


@login_required
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'BaseApp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def see_profile(request):
    user = request.user
    return render(request, 'BaseApp/profile.html',{
        "user":user
    })

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return render(request, 'BaseApp/login.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'BaseApp/register.html',{
        'form':form
    })