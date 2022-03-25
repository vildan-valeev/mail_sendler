import csv
from celery import shared_task
from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile

from mail.models import Follower


def task_import_csv(file: InMemoryUploadedFile, group_id):
    if not group_id:
        return "Import CSV is possible, when  this group will be created...", messages.WARNING
    reader = csv.reader(file)
    Follower.objects.bulk_create(
        [Follower(first_name=i[0], last_name=i[1], b_date=i[2], email=i[3], group_id=group_id) for i in
         reader])


@shared_task
def add(x, y):
    return x + y
