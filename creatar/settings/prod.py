import os

from externship.settings.base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

DEBUG = False

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

# PROD - secret for github auth
SOCIAL_AUTH_GITHUB_KEY = "6f89338e548987acd8da"
SOCIAL_AUTH_GITHUB_SECRET = "ca06cc4aeb263bba25eac26981cd0d47b76bd7cc"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

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


BROKER = f"redis://{REDIS_HOST}:{REDIS_PORT}"


S3_STATIC_STORAGE = os.getenv("S3_STATIC_STORAGE")

# aws settings
AWS_S3_REGION_NAME = "eu-west-1"
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_STORAGE_BUCKET_NAME = S3_STATIC_STORAGE
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

# s3 static settings
STATIC_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
STATICFILES_STORAGE = "vmps_backend.storage_backends.StaticStorage"