from django.urls import path
from .views import enqueue_task, TaskViewSet

urlpatterns = [
    # path("enqueue/", enqueue_task, name="enqueue_task"),
    path("enqueue/", TaskViewSet.as_view({"get": "create"}), name="enqueue_task"),
    path(
        "recent_tasks/",
        TaskViewSet.as_view({"get": "recent_tasks"}),
        name="recent_tasks",
    ),
]
