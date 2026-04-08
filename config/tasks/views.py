from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import FormRegister
from .models import Task

# Register a new user
def register(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = FormRegister()

    return render(request, 'tasks/register.html', {'form': form})

# User login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('list')

    return render(request, 'tasks/login.html')

# Logout user
def user_logout(request):
    logout(request)
    return redirect('login')

# List all tasks
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create a new task
@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description,
            user=request.user
        )

        messages.success(request, "Task created successfully!")
        return redirect('task_list')
    
    return render(request, 'tasks/create.html')

# Delete a task
@login_required
def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

# Update a task
@login_required
def task_update(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})

