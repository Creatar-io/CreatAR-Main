# ====# IMPORTS #====
from django.db import models
from django.contrib.auth.models import User
from core.models.organisation_moderator import OrganisationModerator

# from django_postgres_extensions.models.fields import ArrayField

# ====# CONSTANTS #====
from django.conf import settings


class Organisation(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Brand logo
    brand_logo = models.FileField(blank=True)

    # Moderator
    moderator = models.ForeignKey(
        OrganisationModerator, on_delete=models.CASCADE, related_name="moderator_of"
    )

    # Unique url for details page
    unique_identifier = models.CharField(
        max_length=30,
        unique=True,
        help_text="Please make sure the name you provide is unique, in lower cap, has no whitespace - to adhere to a good API design.",
    )

    # Details
    brand_name = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=75, blank=True)
    services = models.CharField(
        max_length=2, choices=settings.ORGANISATION_SERVICE_CHOICES, default="FO"
    )
    about_company = models.TextField()
    organization_website = models.URLField()

    # Social Handles


    def __str__(self) -> str:
        return str(self.brand_name)

    class Meta:
        ordering = ["created_at"]
