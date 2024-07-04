from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return f"{self.title} -> {self.is_done}"

    class Meta:
        db_table = 'todo'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'