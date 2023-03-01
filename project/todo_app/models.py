from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'