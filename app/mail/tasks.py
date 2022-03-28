from typing import List

from django.core import mail
from django.template.loader import render_to_string

from mail.models import Follower, EmailSendler
from src.celery import app


@app.task
def process_task_import_csv(rows, group_id):
    Follower.objects.bulk_create(
        [Follower(first_name=i[0], last_name=i[1], b_date=i[2], email=i[3], group_id=group_id) for i in rows]
    )
    return 1


@app.task
def process_sends_emails(followers: List[dict], instance_id: int):
    sendler = EmailSendler.objects.filter(pk=instance_id).first()
    html_template = sendler.html_template.html_template.path

    connection = mail.get_connection()
    connection.open()

    # messages = [EmailMultiAlternatives(...) for f in followers]
    messages = [mail.EmailMultiAlternatives(
        subject=sendler.subject,
        body=sendler.text,
        from_email=sendler.from_email,
        to=[f.get('email')],
        connection=connection,
        alternatives=[(render_to_string(html_template, f), "text/html")])
        for f in followers]

    connection.send_messages(messages)
    # The connection was already open so send_messages() doesn't close it.
    # We need to manually close the connection.
    connection.close()
