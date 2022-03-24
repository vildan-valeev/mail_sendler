import csv

from django.contrib import messages

from mail.models import Follower


def save_csv(file, group_id):  # file: InMemoryUploadedFile  ->
    if not group_id:
        return "Import CSV is possible, when  this group will be created...", messages.WARNING
    reader = csv.reader(file)
    Follower.objects.bulk_create(
        [Follower(first_name=i[0], last_name=i[1], b_date=i[2], email=i[3], group_id=group_id) for i in
         reader])

    return "Your csv file has been imported", messages.INFO
