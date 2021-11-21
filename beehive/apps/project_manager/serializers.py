from rest_framework import serializers

from apps.project_manager.models import (
    Project,
    ProjectMember,
    Sprint,
    Task,
    TaskStatus,
    TaskAttachment,
    TaskComment,
    TaskCommentAttachment,
)


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
        fields = ("name", "description")


class TaskAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAttachment
        fields = ("file",)


class TaskSerializer(serializers.ModelSerializer):
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "sprint",
            "status",
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
        fields = ("file",)


class TaskCommentSerializer(serializers.ModelSerializer):
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = TaskComment
        fields = ("user", "comment")

    def get_attachment(self, instance):
        if hasattr(instance, "task_comment_attachment"):
            return TaskAttachmentSerializer(instance.task_comment_attachment).data
        return []
