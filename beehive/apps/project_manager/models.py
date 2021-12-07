from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.base.models import BaseModel
from apps.user.models import User


class ProjectPermission(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    view = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title} ({self.view} - {self.action})"


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    member = models.ManyToManyField(
        User, through="ProjectMember", related_name="project_member"
    )
    code = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.name


class ProjectRole(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    permission = models.ManyToManyField(ProjectPermission)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} ({self.project})"


class ProjectMember(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects_role"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_member"
    )
    role = models.ForeignKey(ProjectRole, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} ({self.project} - {self.role.name})"

    class Meta:
        unique_together = ["user", "project"]
        ordering = ["created_at"]
        verbose_name = _("Project Member")
        verbose_name_plural = _("Project Member")


class Sprint(BaseModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_sprint"
    )
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}({self.project})"


class TaskStatus(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_task"
    )
    sort_order = models.PositiveIntegerField()
    is_todo = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.project})"

    class Meta:
        ordering = ("sort_order",)


class Task(BaseModel):
    PRIOTITY = (
        ("very_high", "Very High"),
        ("high", "High"),
        ("medium", "Meidum"),
        ("low", "Low"),
        ("very_low", "Very Low"),
    )
    task_id = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        TaskStatus, on_delete=models.CASCADE, related_name="status_task"
    )
    priority = models.CharField(choices=PRIOTITY, max_length=50)
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
    estimated_time = models.DecimalField(
        help_text="Estimate Time in hours", decimal_places=2, max_digits=2
    )

    def __str__(self) -> str:
        return f"{self.title}({self.sprint.name} - {self.sprint.project})"


class UserTaskLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_log")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="user_log")
    date = models.DateField()
    time_spent = models.DecimalField(
        help_text="Time Spent in hours", decimal_places=2, max_digits=2
    )
    remaining_time = models.DecimalField(
        help_text="Remaining Time in hours", decimal_places=2, max_digits=2
    )

    class Meta:
        unique_together = ("user", "task", "date")


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
