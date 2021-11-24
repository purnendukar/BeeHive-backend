from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.project_manager.models import (
    Project,
    Sprint,
    Task,
    ProjectMember,
    ProjectRole,
    ProjectPermission,
)
from apps.project_manager.serializers import (
    ProjectSerializer,
    SprintSerializer,
    TaskSerializer,
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

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            project=self.kwargs.get("project_id"),
            project__member__in=[self.request.user],
        )


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

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions += [ProjectMemberPermission()]
        return permissions

    filterset_fields = ("project",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
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

    filterset_fields = ("sprint",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            sprint__project__member__in=[self.request.user],
        )
