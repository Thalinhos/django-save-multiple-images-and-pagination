from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # campo legada presente na migração inicial; preservamos para compatibilidade
    image = models.ImageField(upload_to='todo_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class TodoImage(models.Model):
    todo = models.ForeignKey(
        Todo,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='todo_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.todo.title} ({self.id})"
