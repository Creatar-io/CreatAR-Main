from email.policy import default
from django.db import models
from django.contrib.auth.models import User, Group
import datetime


class Podcast(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associate Moderator User
    moderator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        related_name="moderated_organisations",
    )

    name = models.CharField(max_length=100)
    uniquename = models.CharField(max_length=100, blank=True, default="")
    uuid = models.CharField(max_length=64)
    website_url = models.URLField()
    display_image = models.FileField()
    github_id = models.CharField(max_length=50)
    ideal_tech_stack = models.CharField(max_length=250)
    about = models.TextField(max_length=250, default="We're adapting the cutting edge technologies, and looking out for skilled professionals.")

    last_date_4_submission = models.DateField(default=datetime.datetime(2022, 4, 30))

    # optionals
    linkedin_url = models.URLField()
    # End of optionals

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["created_at"]
