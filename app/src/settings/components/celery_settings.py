from datetime import timedelta

BROKER_URL = 'redis://127.0.0.1:6379'
BROKER_TRANSPORT = 'redis'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 604800}

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_BROKER_TRANSPORT = 'redis'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 604800}

CELERY_RESULT_BACKEND = BROKER_URL

CELERY_TASK_RESULT_EXPIRES = timedelta(days=1)  # Take note of the CleanUp task in middleware/tasks.py
CELERY_MAX_CACHED_RESULTS = 1000
# CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_TRACK_STARTED = True
CELERY_SEND_EVENTS = True
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

REDIS_CONNECT_RETRY = True
REDIS_DB = 0
BROKER_POOL_LIMIT = 2
CELERYD_CONCURRENCY = 1
CELERYD_TASK_TIME_LIMIT = 600
#
# CELERY_BEAT_SCHEDULE = {
#     'task-number-one': {
#         'task': 'messaging.tasks.task_number_one',
#         'schedule': crontab(minute='*/1')
#     },
#     'task-number-two': {
#         'task': 'messaging.tasks.task_number_two',
#         'schedule': crontab(minute='*/1')
#     }
# }
