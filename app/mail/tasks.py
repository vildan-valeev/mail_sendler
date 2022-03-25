import csv
import time

from mail.models import Follower
from src.celery import app


@app.task
def process_task_import_csv(rows, group_id):
    Follower.objects.bulk_create(
        [Follower(first_name=i[0], last_name=i[1], b_date=i[2], email=i[3], group_id=group_id) for i in rows]
    )
    return 1
