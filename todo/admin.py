from django.contrib import admin
from .models import TodoModel

# Register your models here.

@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_done')