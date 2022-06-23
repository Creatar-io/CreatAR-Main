# ====# IMPORTS #====
from django.db import models
from django.contrib.auth.models import User

# from django_postgres_extensions.models.fields import ArrayField

# ====# CONSTANTS #====
from django.conf import settings


class Organisation(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Brand logo
    brand_logo = models.FileField(blank=True)

    # Unique url for details page
    unique_identifier = models.CharField(
        max_length=30,
        unique=True,
        help_text="Please make sure the name you provide is unique, in lower cap, has no whitespace - to adhere to a good API design.",
    )
    # Organizing University
    brand_name = models.CharField(max_length=100)

    # University location
    tag_line = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=75, blank=True)
    services = models.CharField(
        max_length=2, choices=settings.ORGANISATION_SERVICE_CHOICES, default="FO"
    )

    # Date
    about_company = models.TextField()

    def __str__(self) -> str:
        return str(self.brand_name)

    class Meta:
        ordering = ["created_at"]
