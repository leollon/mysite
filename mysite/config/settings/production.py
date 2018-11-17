import os
import getpass
from pathlib import Path

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from mysite.config.settings.common import (
    BASE_DIR, INSTALLED_APPS, TEMPLATES, MIDDLEWARE, WSGI_APPLICATION,
    AUTH_PASSWORD_VALIDATORS, PASSWORD_HASHERS, LANGUAGE_CODE, TIME_ZONE,
    USE_I18N, USE_L10N, USE_TZ, PER_PAGE, ALLOWED_CONTENT, AUTH_USER_MODEL,
    AUTHENTICATION_BACKENDS, SITE_ID, ADMINS)

environ = {
    'SECRET_KEY': "this_key_is_needed_by_django.",
    'SERIAL_SECRET_KEY': "this_key_is_for_itsdangerous",
    'DB_USER': "your_DB_user",
    'DB_PWD': "your_DB_password",
    'EMAIL_USER': "your_email_account",
    'EMAIL_PWD': "your_email_authentication_password",
    'EMAIL_HOST': "your_email_host",
}

SECRET_KEY = environ.get('SECRET_KEY')
SERIAL_SECRET_KEY = environ.get('SERIAL_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['your_test_domain_name']

DOMAIN_NAME = ALLOWED_HOSTS[0]

ROOT_URLCONF = 'mysite.config.urls.production'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PWD'),
    }
}

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'OPTIONS': {
            'MAX_ENTRIES': 1024,
        }
    },
    "redis": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# tied to app's static, like my_app/static/
STATIC_URL = '/assets/'

# Directory containing all static files
# when running `python manage.py collectstatic`, collect all static file in a
# same directory.
# for production deployed, use nginx to response static file requested
STATIC_ROOT = str(Path('/home/')/getpass.getuser()/'assets')

# Here stores all static files
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'assets')
]

# Cache-related
SESSION_CACHE_ALIAS = "redis"
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"


# In order to preventing XSS, it needs to set `ALLOWED_CONTENT`
ALLOWED_CONTENT = {
    'ALLOWED_TAGS': [
        'blockquote', 'ul', 'li', 'ol', 'pre', 'code', 'p', 'h1', 'h2', 'h3',
        'h4', 'h5', 'h6', 'a', 'q', 'section', 'img', 'table', 'thead',
        'tbody', 'tr', 'th', 'td'
    ],
    'ALLOWED_ATTRIBUTES': {
        '*': ['class', 'style'],
        'a': ['href'],
        'img': ['src', 'alt', 'width', 'height'],
    },
    'ALLOWED_STYLES': [
        'color',
        'background-image',
        'background',
        'font',
        'text-align',
    ]
}

# Customize user model
AUTH_USER_MODEL = 'user.User'

# Customize backend authentication
AUTHENTICATION_BACKENDS = [
    'apps.user.backend.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Email account
EMAIL_ACCOUNT = {
    'EMAIL_HOST_USER': environ.get("EMAIL_USER"),
    'EMAIL_HOST_PASSWORD': environ.get('EMAIL_PWD')
}

# Email server related
EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT = environ.get('EMAIL_PORT')
EMAIL_USE_TLS = True

# Email message content template related
EMAIL_RELATED = {
    'REG_NOTIFICATION_FILE': 'notification',
    'PWD_CHANGE_NOTIFICATION_FILE': 'pwd_change',
    'COMMENT_NOTIFICATION': 'comment_notification_template',
}

CSRF_USE_SESSIONS = True  # store csrftoke in the session
CSRF_COOKIE_SECURE = True  # only sent with an HTTPS connection
CSRF_COOKIE_HTTPONLY = True  # csrftoken disallow to be read by JS in console
CSRF_COOKIE_AGE = 604800  # in seconds
SESSION_COOKIE_AGE = 604800  # in seconds
SECURE_CONTENT_TYPE_NOSNIFF = True # 'x-content-type-options: nosniff' header
SECURE_BROWSER_XSS_FILTER = True # 'x-xss-protection: 1; mode=block' header
SESSION_COOKIE_SECURE = True # Using a secure-only session cookie
X_FRAME_OPTIONS = 'DENY' # unless there is a good reason for your site to serve other parts of itself in a frame, you should change it to 'DENY'

# Logger: show more details
LOG_LEVEL = "ERROR"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(module)s] pid:%(process)d [%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s pid:%(process)d [%(message)s]'
        },
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['file',],
            'propagate': True,
        },
        'django': {
            'level': LOG_LEVEL,
            'handlers': ['file',],
            'propagate': True,
        },
        'django.request': {
            'level': LOG_LEVEL,
            'handlers': ['file',],
            'propagate': False,
        },
        'django.db.backends': {
            'level': LOG_LEVEL,
            'handlers': ['file', 'mail_admins'],
            'propagate': False
        }
    },
    # Control over which log records are passed from logger to handler.
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': str(Path(BASE_DIR).parent / 'log' / 'production.log'),
            'filters': ['require_debug_true'],
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': LOG_LEVEL,
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_true'],
            'include_html': True,
        }
    },
}

sentry_sdk.init(dsn="", integrations=[DjangoIntegration()])
