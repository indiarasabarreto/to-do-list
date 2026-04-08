from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Task


# Register a new user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

# User login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('list')
    
    return render(request, 'tasks/login.html')

# User logout
def user_logout(request):
    logout(request)
    return redirect('login')


# List all tasks
@login_required
def list_all_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})

# Create a new task
@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        Task.objects.create(
            title=title, 
            description=description,
            user=request.user
        )
        messages.success(request, "Tarefa criada com sucesso!")
        return redirect('list')

    return render(request, 'tasks/create.html')

# Delete a task
@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('list')

# Update a task
@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('list')

    return render(request, 'tasks/update.html', {'task': task})
