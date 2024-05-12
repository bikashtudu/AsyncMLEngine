# tasks.py in your Django app

import logging
from celery import shared_task
from api.models import Task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import random
import time


@shared_task
def process_task(task_id):
    task = Task.objects.get(id=task_id)
    task.status = "processing"
    task.save()
    # Simulate a task processing
    try:
        # Simulate task processing
        sleep_time = random.randint(3, 10)
        time.sleep(sleep_time)
        result = {"data": "This is the result of the task."}  # Actual logic goes here
        task.result = json.dumps(result)
        task.status = "completed"
        task.save()
        message = f"Task {task.id} completed successfully."
    except Exception as e:
        task.status = "failed"
        task.save()
        message = f"Task {task.id} failed: {str(e)}"

    # Send completion message via WebSocket
    channel_layer = get_channel_layer()
    logger = logging.getLogger(__name__)
    logger.info(f"{task.id}: Sending message to user_{task.user.id}")
    async_to_sync(channel_layer.group_send)(
        f"user_{task.user.id}",  # Assuming the task model has a user field
        {"type": "task_message", "message": message},
    )

    return task.result
