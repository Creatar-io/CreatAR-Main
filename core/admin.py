from django.contrib import admin

# Register your models here.
from core.models.podcast import Podcast
from core.models.organisation import Organisation


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


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "moderators",
        "brand_name",
        "tag_line",
        "location",
        "services",
        "about_company",
    )
    search_fields = ("title", "moderators", "brand_name")
    ordering = ("created_at",)
