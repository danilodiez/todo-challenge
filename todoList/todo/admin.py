from django.contrib import admin

from .models import Task

admin.site.site_header = "Administrador de ToDo's"

admin.site.register(Task)