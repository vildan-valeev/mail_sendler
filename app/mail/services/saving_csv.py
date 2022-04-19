import csv
import io
from itertools import islice

from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile

from mail.tasks import process_task_import_csv


def save_csv(csv_file: InMemoryUploadedFile, group_id: str):
    if not group_id:
        return "Import CSV is possible, when  this group will be created...", messages.WARNING

    decoded_file = csv_file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    data_reader = csv.reader(io_string)

    batch_size = 5000

    while True:
        batch = [row for row in islice(data_reader, batch_size)]
        if not batch:
            break
        process_task_import_csv.delay(batch, int(group_id))

    return "Your csv file will be imported...", messages.INFO
