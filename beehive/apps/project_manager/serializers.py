from rest_framework import serializers

from apps.base.serializers import DynamicFieldsModelSerializer
from apps.user.serializers import UserSerializer
from apps.project_manager.models import (
    Project,
    ProjectPermission,
    ProjectRole,
    ProjectMember,
    Sprint,
    Task,
    TaskStatus,
    TaskAttachment,
    TaskComment,
    TaskCommentAttachment,
)


class ProjectPermissionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProjectPermission
        fields = ("id", "title", "description")


class ProjectRoleSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProjectRole
        fields = ("id", "name", "description", "permission")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["permission"] = ProjectPermissionSerializer(
            instance.permission.all(), many=True
        ).data
        return data


class ProjectMemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ("id", "project", "user", "role")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = UserSerializer(instance.user).data
        data["role"] = ProjectRoleSerializer(instance.role).data
        return data


class ProjectSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description")


class SprintSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Sprint
        fields = (
            "id",
            "number",
            "name",
            "description",
            "project",
            "start_date",
            "end_date",
        )


class TaskStatusSerialier(DynamicFieldsModelSerializer):
    class Meta:
        model = TaskStatus
        fields = (
            "id",
            "name",
            "description",
            "sort_order",
            "is_todo",
            "is_complete",
            "project",
        )


class TaskAttachmentSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TaskAttachment
        fields = (
            "id",
            "file",
        )


class TaskSerializer(DynamicFieldsModelSerializer):
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "sprint",
            "status",
            "parent",
            "depedency",
            "assignee",
            "reporter",
            "attachment",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["status"] = TaskStatusSerialier(
            instance.status,
            fields=(
                "id",
                "name",
                "description",
            ),
        ).data
        data["assignee"] = UserSerializer(instance.assignee).data
        return data

    def get_attachment(self, instance):
        if hasattr(instance, "task_attachment"):
            return TaskAttachmentSerializer(instance.task_attachment, many=True).data
        return []


class TaskCommentAttachmentSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TaskCommentAttachment
        fields = (
            "id",
            "file",
        )


class TaskCommentSerializer(DynamicFieldsModelSerializer):
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = TaskComment
        fields = ("id", "user", "comment")

    def get_attachment(self, instance):
        if hasattr(instance, "task_comment_attachment"):
            return TaskAttachmentSerializer(instance.task_comment_attachment).data
        return []
