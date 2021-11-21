from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins

from apps.project_manager.models import Project, Sprint, Task, ProjectMember
from apps.project_manager.serializers import (
    ProjectSerializer,
    SprintSerializer,
    TaskSerializer,
    ProjectMemberSerializer,
)
from apps.base.mixins import MultiSerializerMixin


class ProjectViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            member__in=[self.request.user],
        )


class ProjectMemberViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            project=self.kwargs.get("project_id"),
            user__in=[self.request.user],
        )


class SprintViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            project__member__in=[self.request.user],
        )


class TaskViewSet(MultiSerializerMixin, ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            sprint__project__member__in=[self.request.user],
        )
