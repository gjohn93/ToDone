from django.urls import path
from projects.views import project_list, detail_view, create_project

urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>/", detail_view, name="show_project"),
    path("create/", create_project, name="create_project"),
]
