from rest_framework import serializers

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


class ProjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPermission
        fields = ("id", "title", "description")


class ProjectRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRole
        fields = ("id", "name", "permission")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["permission"] = ProjectPermissionSerializer(
            instance.permission.all(), many=True
        ).data
        return data


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ("id", "project", "user", "role")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description")


class SprintSerializer(serializers.ModelSerializer):
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


class StatusSerialier(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ("id", "name", "description")


class TaskAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAttachment
        fields = (
            "id",
            "file",
        )


class TaskSerializer(serializers.ModelSerializer):
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
        data["status"] = StatusSerialier(instance.status).data
        return data

    def get_attachment(self, instance):
        if hasattr(instance, "task_attachment"):
            return TaskAttachmentSerializer(instance.task_attachment, many=True).data
        return []


class TaskCommentAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCommentAttachment
        fields = (
            "id",
            "file",
        )


class TaskCommentSerializer(serializers.ModelSerializer):
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = TaskComment
        fields = ("id", "user", "comment")

    def get_attachment(self, instance):
        if hasattr(instance, "task_comment_attachment"):
            return TaskAttachmentSerializer(instance.task_comment_attachment).data
        return []
