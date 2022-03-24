from django.core.mail import EmailMultiAlternatives
from django.forms import model_to_dict
from django.template.loader import render_to_string

from mail.models import EmailSendler


def send_emails(instance_id):

    # if not html_template:
    #     pass
    # followers = Follower.objects.filter(group_id=instance_id).first()
    sendler = EmailSendler.objects.filter(pk=instance_id).first()
    print('sendler', sendler)
    html_template = sendler.html_template.html_template.path
    print('html_template', html_template, type(html_template))
    followers = sendler.follower_group.follower_set.all()
    print('followers', followers)

    for f in followers:
        subject, from_email, to = sendler.subject, sendler.from_email, f.email
        text_content = sendler.text
        html_content = render_to_string(html_template, model_to_dict(f))
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # conn = get_connection(backend=settings.EMAIL_BACKEND,)
        # conn.send_messages([dict_to_email(message)])

    print('SENDING EMAIL')
