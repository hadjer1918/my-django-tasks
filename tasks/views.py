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
            task.save() # This saves the task to the database
            return redirect('task_list') # Refresh the page to show new task
    else:
        form = TaskForm()

    tasks = Task.objects.filter(user=request.user).order_by('completed','-created_at')
    count = tasks.filter(completed=False).count()
    return render(request, 'tasks/list.html', {'tasks': tasks, 'form': form,'count':count})
@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk , user= request.user)
    task.completed = True
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