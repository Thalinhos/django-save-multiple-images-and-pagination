from django.contrib import admin
from .models import Todo, TodoImage


class TodoImageInline(admin.TabularInline):
    model = TodoImage
    extra = 1  # quantos campos vazios aparecem


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'completed')
    search_fields = ('title', 'description')
    inlines = [TodoImageInline]


@admin.register(TodoImage)
class TodoImageAdmin(admin.ModelAdmin):
    list_display = ('todo', 'uploaded_at')
