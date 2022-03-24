from datetime import datetime, timedelta
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '%^n&z9jc3%_v=l$pgeh#qb)u1#^%6c0+o4z@p9py0$q-k8_m(6'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'mail.apps.MailConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "media" / "html_templates", ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'EMAIL_HOST'
EMAIL_PORT = 'EMAIL_PORT'
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
EMAIL_USE_TLS = False
EMAIL_USE_SS = False
EMAIL_TIMEOUT = None
EMAIL_SSL_KEYFILE = None
EMAIL_SSL_CERTFILE = None

# ----------------------------------------- CELERY -----------------------------------------------
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
