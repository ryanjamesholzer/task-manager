from django.urls import path
from tasks.views import (
    create_task,
    list_tasks,
    show_task,
    create_task_note,
)


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("mine/<int:id>/", show_task, name="show_task"),
    path(
        "mine/<int:id>/notes/create/",
        create_task_note,
        name="create_task_note",
    ),
]
