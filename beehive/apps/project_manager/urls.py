from rest_framework.routers import DefaultRouter

from apps.project_manager.apis import (
    ProjectViewSet,
    SprintViewSet,
    TaskViewSet,
    ProjectMemberViewSet,
    ProjectRoleViewSet,
    TaskStatusViewSet,
    ProjectPermissionViewSet,
)


default_router = DefaultRouter(trailing_slash=False)

default_router.register(
    r"projects/(?P<project_id>[^/.]+)/members",
    ProjectMemberViewSet,
    basename="project_members",
)
default_router.register(
    r"projects/(?P<project_id>[^/.]+)/roles",
    ProjectRoleViewSet,
    basename="project_role",
)
default_router.register(
    r"projects/(?P<project_id>[^/.]+)/status",
    TaskStatusViewSet,
    basename="project_status",
)
default_router.register(
    r"projects/(?P<project_id>[^/.]+)/sprints",
    SprintViewSet,
    basename="project_sprints",
)
default_router.register("projects", ProjectViewSet, basename="project")
default_router.register("tasks", TaskViewSet, basename="task")
default_router.register(
    "permissions", ProjectPermissionViewSet, basename="project_permission"
)


urlpatterns = default_router.urls
