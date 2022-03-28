from itertools import islice

from mail.models import EmailSendler
from mail.tasks import process_sends_emails


def send_emails(instance_id):
    # if not html_template:
    #     pass

    sendler = EmailSendler.objects.filter(pk=instance_id).first()
    followers = sendler.follower_group.follower_set.all()

    batch_size = 5000
    while True:
        batch = [row for row in islice(followers, batch_size)]
        if not batch:
            break
        process_sends_emails.delay(batch, int(instance_id))

    print('SENDING EMAIL')


def send_delayed_emails(instance_id):
    """Отправка отложенных записей"""
    # аналогично send_emails. только на @shared_task
    pass
