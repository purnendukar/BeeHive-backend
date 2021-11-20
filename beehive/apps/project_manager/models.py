from django.db import models

from apps.base.models import BaseModel
from beehive.apps.user.models import User


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Sprint(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class Status(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Task(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    # parent = models.ForeignKey("self", on_delete=models.CASCADE)
    depedency = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class TaskAttachment(BaseModel):
    task = models.ForeignKey(Task)
    file = models.FileField(null=True, blank=True)


class TaskComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    attachment = models.FileField(null=True, blank=True)
