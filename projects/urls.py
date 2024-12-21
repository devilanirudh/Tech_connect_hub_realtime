from .views import projects, project,createProject,updateproject,deleteproject
from django.urls import path


urlpatterns = [
    path("", projects, name="projects"),
    path("project/<str:pk>/", project, name="project"),
    path("create-project/", createProject, name="create-project"),
    path("update-project/<str:pk>/", updateproject, name="updateproject"),
    path("delete-project/<str:pk>/", deleteproject, name="deleteproject"),
]
