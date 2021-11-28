from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from apps.user.apis import AuthViewset


default_router = DefaultRouter(trailing_slash=False)

default_router.register("auth", AuthViewset, basename="auth")

urlpatterns = [
    path("plans/", include("apps.plan.urls"), name="plan"),
    path(
        "project-manager/", include("apps.project_manager.urls"), name="project_manager"
    ),
]
urlpatterns += default_router.urls
