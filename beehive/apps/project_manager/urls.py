from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from apps.project_manager.apis import (
    ProjectViewSet,
    SprintViewSet,
    TaskViewSet,
    ProjectMemberViewSet,
    ProjectRoleViewSet,
    ProjectPermissionViewSet,
)


default_router = DefaultRouter(trailing_slash=False)

default_router.register(
    r"project/(?P<project_id>[^/.]+)/member",
    ProjectMemberViewSet,
    basename="project_members",
)
default_router.register(
    r"project/(?P<project_id>[^/.]+)/roles",
    ProjectRoleViewSet,
    basename="project_role",
)
default_router.register("project", ProjectViewSet, basename="project")
default_router.register("sprint", SprintViewSet, basename="sprint")
default_router.register("task", TaskViewSet, basename="task")
default_router.register(
    "permissions", ProjectPermissionViewSet, basename="project_permission"
)


urlpatterns = default_router.urls
