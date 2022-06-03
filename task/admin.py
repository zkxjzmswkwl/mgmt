from django.contrib import admin
from .models import Task, TaskUpdate

admin.site.register(Task)
admin.site.register(TaskUpdate)
