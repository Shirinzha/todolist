from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_date = models.DateField()

    def __str__(self):
        return self.title