from django.forms import ModelForm
from core.models.organisation import Organisation
from core.models.organisation_moderator import OrganisationModerator

# Create the form class.
class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = [
            "brand_logo",
            "unique_identifier",
            "brand_name",
            "tag_line",
            "location",
            "services",
            "about_company",
            "organization_website"
        ]


# Organisation moderator POC collection
class OrganisationModeratorForm(ModelForm):
    class Meta:
        model = OrganisationModerator
        fields = [
            "contact_number",
            "position_in_company",
            "contact_number",
            "conset_for_communication",
        ]
