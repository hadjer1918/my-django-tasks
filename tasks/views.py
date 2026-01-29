from django.shortcuts import render, redirect,get_object_or_404 # Add redirect here
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm # Import your new form
from django.http import HttpResponse
from django.contrib.auth.models import User
@login_required
def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    tasks = Task.objects.filter(user=request.user).order_by('completed', '-priority', '-created_at')
    
    total_count = tasks.count()
    completed_count = tasks.filter(completed=True).count()
    left_count = total_count - completed_count
    progress = int((completed_count / total_count * 100)) if total_count > 0 else 0
    
    from django.utils import timezone
    today = timezone.now().date()
    
    return render(request, 'tasks/list.html', {
        'tasks': tasks, 
        'form': form, 
        'count': left_count,
        'progress': progress,
        'completed_count': completed_count,
        'today': today
    })

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update.html', {'form': form, 'task': task})

@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk , user= request.user)
    task.completed = not task.completed # Toggle completion
    task.save()
    return redirect('task_list')
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    task.delete()
    return redirect('task_list')
def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        return HttpResponse("Admin created! User: admin, Pass: admin123")
    return HttpResponse("Admin already exists.")