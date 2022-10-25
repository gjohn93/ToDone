from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create.html", context)

@login_required
def show_my_tasks(request):
    my_tasks = Task.objects.filter(assignee = request.user)
    context = {
        "my_task_list" : my_tasks
    }
    return render(request, "tasks/mine.html", context)
