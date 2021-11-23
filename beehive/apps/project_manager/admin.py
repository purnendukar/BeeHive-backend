from django.contrib import admin

from apps.project_manager.models import (
    Project,
    ProjectMember,
    ProjectRole,
    Sprint,
    Task,
    TaskStatus,
    ProjectPermission,
)


# Register your models here.
class ProjectMemberInline(admin.StackedInline):
    model = ProjectMember
    can_delete = False
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectMemberInline,)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPermission)
admin.site.register(ProjectRole)
admin.site.register(ProjectMember)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(TaskStatus)
