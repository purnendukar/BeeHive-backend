from django.contrib import admin

from apps.project_manager.models import Project, ProjectMember, ProjectRole


# Register your models here.
class ProjectMemberInline(admin.StackedInline):
    model = ProjectMember
    can_delete = False
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectMemberInline,)
    # pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRole)
