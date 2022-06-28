# Imports
from rest_framework import serializers
from core.models.organisation import Organisation
from core.models.organisation_moderator import OrganisationModerator


class OrganisationSerializer(serializers.ModelSerializer):
    moderator = serializers.SlugRelatedField(
        queryset=OrganisationModerator.objects.all(), slug_field="moderator_of"
    )

    class Meta:
        model = Organisation
        fields = [
            "brand_logo",
            "moderator",
            "unique_identifier",
            "brand_name",
            "tag_line",
            "location",
            "services",
            "location",
            "about_company",
            "organization_website",
        ]
