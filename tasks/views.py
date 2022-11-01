from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, TaskNoteForm
from tasks.models import Task

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def create_task_note(request, id):
    if request.method == "POST":
        form = TaskNoteForm(request.POST)
        if form.is_valid():
            task_note = form.save(False)
            task_note.task = Task.objects.get(id=id)
            task_note.is_completed = False
            task_note.save()
            return redirect("show_task", id=id)
    else:
        form = TaskNoteForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/notes/create.html", context)


@login_required
def list_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": tasks,
    }
    return render(request, "tasks/list.html", context)


@login_required
def show_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        "task": task,
    }
    return render(request, "tasks/detail.html", context)


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return redirect(request, "tasks/edit.html", context)
