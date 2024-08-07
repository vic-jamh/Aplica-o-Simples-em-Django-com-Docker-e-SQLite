from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)  # False indica que a tarefa está pendente

    def __str__(self):
        return self.title
