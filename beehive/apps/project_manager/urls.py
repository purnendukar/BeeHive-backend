from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from apps.project_manager.apis import ProjectViewSet, SprintViewSet, TaskViewSet


default_router = DefaultRouter(trailing_slash=False)

default_router.register("project", ProjectViewSet, basename="project")
default_router.register("sprint", SprintViewSet, basename="sprint")
default_router.register("task", TaskViewSet, basename="task")

urlpatterns = default_router.urls
