from django.db.models.signals import post_save
from django.dispatch import receiver

from mail.models import EmailSendler, Follower
from mail.services.sending_emails import send_emails, send_delayed_emails


@receiver(post_save, sender=EmailSendler)
def order_publication(sender, instance:EmailSendler, created, **kwargs):
    if created:
        print('SIGNAL')
        if not instance.delayed:
            send_emails(instance.id)
        else:
            send_delayed_emails(instance.id)
