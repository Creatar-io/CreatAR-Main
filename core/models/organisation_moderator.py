# ====# IMPORTS #====
from django.db import models
from django.contrib.auth.models import User

# from django_postgres_extensions.models.fields import ArrayField

# ====# CONSTANTS #====
from django.conf import settings


class OrganisationModerator(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated user | Check user email_verified to track moderator authenticity
    meta = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="moderator_of",
    )

    # Position in company
    position_in_company = models.TextField(blank=True, max_length=200)

    # Contact
    contact_number = models.CharField(max_length=15, blank=True)

    # Opt-in
    conset_for_communication = models.BooleanField(
        verbose_name="I agree to be contacted later on by team Creatar for verification.",
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.meta)

    class Meta:
        ordering = ["created_at"]
