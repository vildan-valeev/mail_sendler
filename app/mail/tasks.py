from celery import shared_task

@shared_task(**TASK_CONFIG)
def send_emails(messages, backend_kwargs=None, **kwargs):
    # backward compat: handle **kwargs and missing backend_kwargs
    combined_kwargs = {}
    if backend_kwargs is not None:
        combined_kwargs.update(backend_kwargs)
    combined_kwargs.update(kwargs)

    # backward compat: catch single object or dict
    if isinstance(messages, (EmailMessage, dict)):
        messages = [messages]

    # make sure they're all dicts
    messages = [email_to_dict(m) for m in messages]

    conn = get_connection(backend=settings.CELERY_EMAIL_BACKEND, **combined_kwargs)
    try:
        conn.open()
    except Exception:
        logger.exception("Cannot reach CELERY_EMAIL_BACKEND %s", settings.CELERY_EMAIL_BACKEND)

    messages_sent = 0

    for message in messages:
        try:
            sent = conn.send_messages([dict_to_email(message)])
            if sent is not None:
                messages_sent += sent
            logger.debug("Successfully sent email message to %r.", message['to'])
        except Exception as e:
            # Not expecting any specific kind of exception here because it
            # could be any number of things, depending on the backend
            logger.warning("Failed to send email message to %r, retrying. (%r)",
                           message['to'], e)
            send_emails.retry([[message], combined_kwargs], exc=e, throw=False)

    conn.close()
    return messages_sent
