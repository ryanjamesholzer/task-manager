from django.forms import ModelForm
from tasks.models import Task, TaskNote


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        ]


class TaskNoteForm(ModelForm):
    class Meta:
        model = TaskNote
        fields = [
            "instruction",
        ]
