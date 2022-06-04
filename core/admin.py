from django.contrib import admin

# Register your models here.
from core.models.podcast import Podcast

@admin.register(Podcast)
class PodcatAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "streamed_on",
        "stream_link",
        "created_at",
    )
    search_fields = ("title", "streamed_on")
    ordering = ("created_at",)