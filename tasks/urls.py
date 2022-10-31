from django.urls import path
from tasks.views import create_task, list_tasks, show_task


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("mine/<int:id>/", show_task, name="show_task"),
]
