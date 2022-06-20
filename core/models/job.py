from django.db import models

class Announcement(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Content for announcement
    title = models.CharField(max_length=75)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
