from email.policy import default
from django.db import models
from django.contrib.auth.models import User, Group
import datetime


class Podcast(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    streamed_on = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # optionals
    stream_link = models.URLField()
    # End of optionals

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["created_at"]
