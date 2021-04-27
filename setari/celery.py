from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setari.settings')

app = Celery('setari')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = { # If I use celery-beat
    'get-joke-every-20-seconds': {
        'task': 'get_the_joke',
        'schedule': 20.0
    }
}

app.autodiscover_tasks()
