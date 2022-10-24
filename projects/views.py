from django.shortcuts import render
from projects.models import Project


def show_project(request):
    project_list = Project.objects.all()
    context = {
        "project_list": project_list,
        "number_of_projects" : len(project_list),
    }

    return render(request, "projects/list.html", context)


# Create your views here.
