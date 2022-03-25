from django.db.models.signals import post_save
from django.dispatch import receiver

from mail.models import EmailSendler, Follower
from mail.services.sending_emails import send_emails


# @receiver(post_save, sender=EmailSendler)
# def order_publication(sender, instance, created, **kwargs):
#     # ыва
#     if created:
#         print('SIGNAL')
#         # TODO: переключить на celery task
#         send_emails(instance.id)



# @receiver(post_save, sender=Follower)
# def order_publication(sender, instance, created, **kwargs):
#     # ыва
#     if created:
#         print('SIGNAL')
#         # TODO: переключить на celery task
#         result = add_test_follower.delay(instance.id)
#         print(result)
#
