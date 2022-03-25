import csv

from django.contrib import messages

from mail.models import Follower
from mail.tasks import task_import_csv


def save_csv(file, group_id):  # file: InMemoryUploadedFile  ->
    if not group_id:
        return "Import CSV is possible, when  this group will be created...", messages.WARNING
    task_import_csv(file, group_id)

    return "Your csv file has been imported", messages.INFO
