from django.contrib import admin

from MyDjangoProject.tasks.models import Task

# admin.site.register(Task)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "is_completed")
    list_filter = ("title",)