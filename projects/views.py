from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
    }

    return render(request, "projects/list.html", context)


@login_required
def detail_view(request, id):
    project_details = Project.objects.get(id=id)
    context = {"project_details": project_details}
    return render(request, "projects/detail.html", context)


# Create your views here.


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create.html", context)
