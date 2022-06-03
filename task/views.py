from django.shortcuts import render
from task.models import Task


def index(request):
    ctx = {
        "task": Task.objects.get(id=1)
    }
    return render(request, "task/index.html", ctx)