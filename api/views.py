from django.shortcuts import render

from django.http import JsonResponse
from .models import Task
from tasks.tasks import process_task
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


def enqueue_task(request):
    task = Task.objects.create()  # Creates a new task with default status 'queued'
    process_task.delay(task.id)  # Sends the task to Celery
    return JsonResponse({"task_id": task.id, "status": "Task queued"})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        process_task.delay(instance.id)

    @action(detail=False, methods=["get"])
    def recent_tasks(self, request):
        recent_tasks = Task.objects.filter(user=request.user).order_by("-created_at")[
            :10
        ]
        serializer = self.get_serializer(recent_tasks, many=True)
        return Response(serializer.data)
