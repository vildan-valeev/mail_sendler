from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


def chunked(iterator, chunksize):
    """
    Yields items from 'iterator' in chunks of size 'chunksize'.
    >>> list(chunked([1, 2, 3, 4, 5], chunksize=2))
    [(1, 2), (3, 4), (5,)]
    """
    chunk = []
    for idx, item in enumerate(iterator, 1):
        chunk.append(item)
        if idx % chunksize == 0:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


class CeleryEmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super(CeleryEmailBackend, self).__init__(fail_silently)
        self.init_kwargs = kwargs

    def send_messages(self, email_messages):
        result_tasks = []
        for chunk in chunked(email_messages, settings.CELERY_EMAIL_CHUNK_SIZE):
            chunk_messages = [email_to_dict(msg) for msg in chunk]
            result_tasks.append(send_emails.delay(chunk_messages, self.init_kwargs))
        return result_tasks
