"""
Django settings for CreatAR project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from os import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-cmz3@v-3t=ef&p*(mgyj4q+zen-3x#gt3!um!bg&q01yv*lpcf"

# App will run in debug mode, unless debug is set False explicitly.
DEBUG = environ.get(key="DEBUG", default=False)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "django_celery_results",
    "django_celery_beat",
    "webshell",
    # 3rd party
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Add your modules here
    "core",
    "home",
    "users",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated",
        # "rest_framework.permissions.IsAdminUser",
    ],
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

SOCIAL_AUTH_URL_NAMESPACE = "social"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True

# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Redirection after login
LOGIN_REDIRECT_URL = "/creatARproTemp"

# LOGIN_URL = "login"
# LOGOUT_URL = "logout"

SITE_ID = 1
# ACCOUNT_LOGOUT_ON_GET = True

# SOCIAL_AUTH_DISCONNECT_PIPELINE = (
#     # Verifies that the social association can be disconnected from the current
#     # user (ensure that the user login mechanism is not compromised by this
#     # disconnection).
#     "social_core.pipeline.disconnect.allowed_to_disconnect",
#     # Collects the social associations to disconnect.
#     "social_core.pipeline.disconnect.get_entries",
#     # Revoke any access_token when possible.
#     "social_core.pipeline.disconnect.revoke_tokens",
#     # Removes the social associations.
#     "social_core.pipeline.disconnect.disconnect",
# )

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "request_logging.middleware.LoggingMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "creatar.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_BASE_DIR, "users", "templates"),
            os.path.join(PROJECT_BASE_DIR, "users", "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "creatar.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console_handler": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "api": {"handlers": ["console_handler"], "level": "INFO", "propagate": False},
        "django": {
            "handlers": ["console_handler"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console_handler"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console_handler"],
        "level": str(os.getenv("DJANGO_LOG_LEVEL", "INFO")).upper(),
        "propagate": False,
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SMTP Backend Configuration
# https://ap-south-1.console.aws.amazon.com/ses/home?region=ap-south-1#/account
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "email-smtp.ap-south-1.amazonaws.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "AKIAT4NVYU36SGJCDSFI"
EMAIL_HOST_PASSWORD = "BOiPz+6NW0jEXyMSlQ20F/C8zj6yYY7+hKb6jj7cJ+cA"
DEFAULT_FROM_EMAIL = "noreply@creatar.io"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

import logging

REQUEST_LOGGING_DATA_LOG_LEVEL = logging.INFO
REQUEST_LOGGING_ENABLE_COLORIZE = False

# allow upload big file
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 15  # 15M
FILE_UPLOAD_MAX_MEMORY_SIZE = DATA_UPLOAD_MAX_MEMORY_SIZE

# Choices for organisation services
ORGANISATION_SERVICE_CHOICES = [
    ("FH", "Fashion"),
    ("MU", "Music"),
    ("BE", "Beauty"),
    ("FM", "FMCG"),
    ("TV", "TV"),
    ("AM", "Automotive"),
    ("SP", "Sport"),
    ("TR", "Travel"),
    ("FO", "Food"),
    ("GA", "Gaming"),
    ("SO", "Social Cause"),
]
