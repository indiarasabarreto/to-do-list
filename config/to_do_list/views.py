from django.shortcuts import render, redirect
from .models import Task

# List all tasks
def list_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

# Create a new task
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        Task.objects.create(
            title=title, 
            description=description
        )
        return redirect('list')

    return render(request, 'tasks/create.html')

# Delete a task
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('list')

# Update a task
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('list')

    return render(request, 'tasks/update.html', {'task': task})
