# Imports
from rest_framework import serializers
from core.models.organisation_moderator import OrganisationModerator


class OrganisationSerializer(serializers.ModelSerializer):
    # moderator = serializers.SlugRelatedField(
    #     queryset=OrganisationModerator.objects.all(), slug_field="moderator_of"
    # )

    class Meta:
        model = OrganisationModerator
        fields = [
            "position_in_company",
            "contact_number",
            "conset_for_communication",
        ]
