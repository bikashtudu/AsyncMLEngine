import os
from celery import Celery
import logging
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asyncmlengine.settings")
django.setup()
logging.warning("something")
app = Celery("asyncmlengine")
# broker_url="amqp://user:securepassword@localhost:5672//")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.config_from_object('asyncmlengine.settings', namespace='CELERY')
# broker_url = "amqp://user:securepassword@localhost:5672//"
# logging.warning(os.environ["CELERY_BROKER_URL"])
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
