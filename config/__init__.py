from __future__ import absolute_import, unicode_literals

# Это обязательно для запуска задач Celery
from .celery import app as celery_app

__all__ = ('celery_app',)
