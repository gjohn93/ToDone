from django.urls import path
from projects.views import project_list, detail_view

urlpatterns = [
    path("", project_list, name= "list_projects"),
    path("<int:id>/", detail_view , name="show_project")
]
