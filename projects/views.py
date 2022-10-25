from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
        "number_of_projects": len(project_list),
    }

    return render(request, "projects/list.html", context)


# Create your views here.
