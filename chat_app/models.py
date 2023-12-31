from django.db import models

# Create your models here.
from django.db import models


class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="任务名称", max_length=65, unique=True)
    status = models.CharField(verbose_name="任务状态", max_length=1, choices=Status.choices)

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"

    def __str__(self):
        return self.name