from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        Task.objects.create(name=name)
    return redirect('task_list')

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.name = request.POST.get('task_name')
        task.save()
        return redirect('task_list')
    return render(request, 'todolist/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')
