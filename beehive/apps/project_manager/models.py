from django.db import models
from django.db.models.fields import related

from apps.base.models import BaseModel
from apps.user.models import User


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Sprint(BaseModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_sprint"
    )
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
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="status_task"
    )
    sprint = models.ForeignKey(
        Sprint, on_delete=models.CASCADE, related_name="sprint_task"
    )
    # parent = models.ForeignKey("self", on_delete=models.CASCADE)
    depedency = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="task_dependency",
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="assigned_task",
    )
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reported_task",
    )


class TaskAttachment(BaseModel):
    task = models.ForeignKey(Task, related_name="task_attachment")
    file = models.FileField(null=True, blank=True)


class TaskComment(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_task_comment"
    )
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="task_comment"
    )
    comment = models.TextField(blank=True)
    attachment = models.FileField(null=True, blank=True)
