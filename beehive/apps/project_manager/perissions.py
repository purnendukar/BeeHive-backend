from rest_framework.permissions import BasePermission


class ProjectMemberPermission(BasePermission):
    def has_permission(self, request, view):
        project_member = request.user.projects_role.all().first()
        if not project_member:
            return False
        return project_member.role.permission.filter(
            view=view.__class__.__name__, action=view.action
        ).exists()
