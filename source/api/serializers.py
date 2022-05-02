from rest_framework import serializers

from webapp.models import Task


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "execution_time"]


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
