from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins

from apps.project_manager.models import Project, Sprint, Task
from apps.project_manager.serializers import (
    ProjectSerializer,
    SprintSerializer,
    TaskSerializer,
)
from apps.base.mixins import MultiSerializerMixin


class ProjectViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            memeber__in=self.request.user,
        )


class SprintViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            project__memeber__in=self.request.user,
        )


class TaskViewSet(MultiSerializerMixin, ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            sprint__project__memeber__in=self.request.user,
        )
