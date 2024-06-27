# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_to_video.settings')

# app = Celery('image_to_video')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_to_video.settings')

app = Celery('image_to_video')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
