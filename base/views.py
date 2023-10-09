from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from base.models import Tasks

# Create your views here.

@never_cache
def UserRegister(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create(username=username, email=email, password=make_password(password))
            login(request, user)
            return redirect("main")
        else:
            return render(request, "Register.html")

@never_cache
def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                messages.error(request, 'Invalid Username or Password')
                return redirect("user-login")
        else:
            return render(request, "Login.html")

@never_cache
@login_required(login_url="user-login")
def main(request):
    curr_user = request.user
    tasks = Tasks.objects.filter(user=curr_user)
    context = {
        "tasks": tasks
    }
    return render(request, "Main.html", context)

@never_cache
@login_required(login_url="user-login")
def UserLogout(request):
    logout(request)
    return redirect('user-login')

@never_cache
@login_required(login_url="user-login")
def AddTask(request):
    if request.method == "POST":
        curr_user = request.user
        date = request.POST.get('date')
        task = request.POST.get('task')
        tasks = Tasks.objects.create(user=curr_user, task=task, date=date)
        return redirect('main')
    else:
        return redirect('main')
    
@never_cache
@login_required(login_url="user-login")
def EditTask(request, id):
    try:
        task_ = Tasks.objects.get(id=id)
        if request.method == "POST":
            date = request.POST.get('date')
            task = request.POST.get('task')
            task_.date = date
            task_.task = task
            task_.save()
            return redirect('main')
        else:
            context =  {
                "task": task_
            }
            return render(request, "EditTask.html", context)
    except:
        return redirect("main")
    
@never_cache
@login_required(login_url="user-login")
def DeleteTask(request, id):
    try:
        task = Tasks.objects.get(id=id)
        task.delete()
        return redirect('main')
    except:
        return redirect('main')
    
@never_cache
@login_required(login_url="user-login")
def TaskComplete(request, id):
    try:
        task = Tasks.objects.get(id=id)
        task.status = True
        task.save()
        return redirect('main')
    except:
        return redirect('main')