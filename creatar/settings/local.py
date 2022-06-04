import os

from creatar.settings.base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

DEBUG = True

# SOCIAL_AUTH_GITHUB_KEY = "6f89338e548987acd8da"
# SOCIAL_AUTH_GITHUB_SECRET = "cc54b17010c071fb6f92dd85651a5bfaf62f8043"
SOCIAL_AUTH_GITHUB_KEY = "6f89338e548987acd8da"
SOCIAL_AUTH_GITHUB_SECRET = "e94e18d49cf383597b6082ed71d625212931f3f7"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "default",
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": "5432",
    }
}

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "home/static"),
]

MEDIA_URL = "media/"
MEDIA_ROOT = "media"
