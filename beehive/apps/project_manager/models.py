from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.base.models import BaseModel
from apps.user.models import User


class ProjectRole(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    member = models.ManyToManyField(
        User, through="ProjectMember", related_name="project_member"
    )

    def __str__(self) -> str:
        return self.name


class ProjectMember(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects_role"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_member"
    )
    role = models.ManyToManyField(ProjectRole)

    class Meta:
        unique_together = ["user", "project"]
        ordering = ["created_at"]
        verbose_name = _("Project Member")
        verbose_name_plural = _("Project Member")


class Sprint(BaseModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_sprint"
    )
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}({self.project})"


class TaskStatus(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        TaskStatus, on_delete=models.CASCADE, related_name="status_task"
    )
    sprint = models.ForeignKey(
        Sprint, on_delete=models.CASCADE, related_name="sprint_task"
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
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

    def __str__(self) -> str:
        return f"{self.title}({self.sprint.name} - {self.sprint.project})"


class TaskAttachment(BaseModel):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="task_attachment"
    )
    file = models.FileField(null=True, blank=True)


class TaskComment(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_task_comment"
    )
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="task_comment"
    )
    comment = models.TextField(blank=True)


class TaskCommentAttachment(BaseModel):
    task_comment = models.ForeignKey(
        TaskComment, on_delete=models.CASCADE, related_name="task_comment_attachment"
    )
    file = models.FileField()
