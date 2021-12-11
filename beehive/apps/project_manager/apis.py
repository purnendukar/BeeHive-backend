from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.project_manager.models import (
    Project,
    Sprint,
    Task,
    TaskStatus,
    ProjectMember,
    ProjectRole,
    ProjectPermission,
)
from apps.project_manager.serializers import (
    ProjectSerializer,
    SprintSerializer,
    TaskSerializer,
    TaskStatusSerialier,
    ProjectMemberSerializer,
    ProjectRoleSerializer,
    ProjectPermissionSerializer,
)
from apps.project_manager.perissions import ProjectMemberPermission


class ProjectViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.action in ["update", "partial_update"]:
            permissions += [ProjectMemberPermission()]
        return permissions

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            member__in=[self.request.user],
        )


class ProjectPermissionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectPermissionSerializer


class ProjectRoleViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = ProjectRole.objects.all()
    serializer_class = ProjectRoleSerializer

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions += [ProjectMemberPermission()]
        return permissions

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter project related data that is associated to user
        return queryset.filter(
            project=self.kwargs.get("project_id"),
            project__member__in=[self.request.user],
        )

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs.get("project_id"))


class ProjectMemberViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.action in ["create", "update", "partial_update"]:
            permissions += [ProjectMemberPermission()]
        return permissions

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter project related data that is associated to user
        return queryset.filter(
            project=self.kwargs.get("project_id"),
            project__member__in=[self.request.user],
        )

    def create(self, request, *args, **kwargs):
        request.data["project"] = self.kwargs.get("project_id")
        return super().create(request, *args, **kwargs)


class SprintViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    search_fields = ("name", "description")
    filterset_fields = {
        "start_date": ["gte", "lte", "exact", "gt", "lt"],
        "end_date": ["gte", "lte", "exact", "gt", "lt"],
        "is_complete": ["exact"],
    }

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions += [ProjectMemberPermission()]
        return permissions

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter member related data
        return queryset.filter(
            project=self.kwargs.get("project_id"),
            project__member__in=[self.request.user],
        )


class TaskViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions += [ProjectMemberPermission()]
        return permissions

    search_fields = ("title", "description")

    filterset_fields = (
        "sprint",
        "sprint__project",
        "status__is_complete",
        "sprint__start_date",
        "sprint__end_date",
        "status",
        "assignee",
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter member related data
        return queryset.filter(
            sprint__project__member__in=[self.request.user],
        )


class TaskStatusViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerialier

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions += [ProjectMemberPermission()]
        return permissions

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter project related data
        return queryset.filter(
            project=self.kwargs.get("project_id"),
            project__member__in=[self.request.user],
        )

    def create(self, request, *args, **kwargs):
        request.data["project"] = kwargs.get("project_id")
        return super().create(request, *args, **kwargs)
