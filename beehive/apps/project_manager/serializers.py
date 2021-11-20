from rest_framework import serializers

from apps.project_manager.models import Project, Sprint, Task
from beehive.apps.project_manager.models import Status, TaskComment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "description"]


class SprintSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Sprint
        fields = ("number", "name", "description", "start_date", "end_date")


class StatusSerialier(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("name", "description")


class TaskSerializer(serializers.ModelSerializer):
    sprint = SprintSerializer(read_only=True)
    status = StatusSerialier(read_only=False)
    depedency = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "sprint",
            "status",
            "depedency",
            "assignee",
            "reporter",
        )


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ("user", "comment", "attachment")
