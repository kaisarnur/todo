from rest_framework.viewsets import ModelViewSet

from webapp.models import Task
from api.serializers import TaskReadSerializer, TaskWriteSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskWriteSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TaskReadSerializer
        return self.serializer_class
