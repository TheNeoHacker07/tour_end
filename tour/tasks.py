from celery import shared_task
from django.utils import timezone
from .models import Tour

@shared_task
def deactivate_expired_tours():
    now = timezone.now()
    expired_tours = Tour.objects.filter(end_date__lt=now, is_active=True)
    expired_tours.update(is_active=False)
