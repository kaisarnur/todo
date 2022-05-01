from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Title")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Description")
    execution_time = models.DateTimeField(null=False, blank=False, verbose_name="Execution Time")
    is_done = models.BooleanField(default=False, verbose_name="Is done")

    def __str__(self):
        return self.title
