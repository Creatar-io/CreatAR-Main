# ====# IMPORTS #====
from django.db import models
from django.contrib.auth.models import User

# from django_postgres_extensions.models.fields import ArrayField

# ====# CONSTANTS #====
from django.conf import settings

from core.models.organisation import Organisation


class OrganisationModerator(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated user
    meta = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="moderator_of",
    )

    # Moderator of
    organisation = models.OneToOneField(
        Organisation, on_delete=models.CASCADE, related_name="moderated_by"
    )

    # Contact
    contact_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.meta)

    class Meta:
        ordering = ["created_at"]
