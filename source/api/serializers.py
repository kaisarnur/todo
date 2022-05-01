from rest_framework import serializers

from webapp.models import Task


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
