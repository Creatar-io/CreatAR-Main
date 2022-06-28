from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


# Importing models
from core.models.podcast import Podcast

# Extract Video-ID from the video URL
video_id_extractor = lambda x: str(x)[str(x).rindex("=") + 1 :]

# Importing forms
from core.froms import OrganisationForm, OrganisationModeratorForm

# Importing models
from core.models.organisation import Organisation
from core.models.organisation_moderator import OrganisationModerator

# Importing model serializers
from core.serializers.organisation_serializer import OrganisationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class OrganisationRegistrationHandler(APIView):
    """
    Organisation registration handler
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Render form
        """
        form = OrganisationForm()
        return render(request, "register_organisation.html", {"form": form})

    def post(self, request, format=None):
        """
        Validate org-registration form, save model, redirect to POC (Org moderator) form
        """
        # create a form instance and populate it with data from the request:
        form = OrganisationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("==#" * 5, "Form Validated.")
            # process the data in form.cleaned_data as required
            form.cleaned_data.update(
                {
                    "moderator": OrganisationModerator(meta=request.user),
                }
            )
            # Serialize
            org_srz = OrganisationSerializer(data=form.cleaned_data)

            print(form.cleaned_data)
            if org_srz.is_valid(raise_exception=True):
                # redirect to a new URL:
                return Response(org_srz.validated_data)

        return Response({"msg": "Failed"})


class OrganisationModeratorRegistrationHandler(APIView):
    """
    Organisation Morderator registration handler
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Render form
        """

        # Fetched logged in user-email
        user_email = None
        print("==#" * 10, request.user)
        print("==#" * 10, request.user.is_authenticated)

        if request.user.is_authenticated:
            user_email = request.user.email
            print("==#" * 10, user_email)

        # Render form
        form = OrganisationModeratorForm()
        return render(
            request,
            "register_organisation_moderator.html",
            {"form": form, "v_email": user_email},
        )

    def post(self, request, format=None):
        """
        Validate org-registration form, save model, redirect to POC (Org moderator) form
        """
        # create a form instance and populate it with data from the request:
        form = OrganisationModeratorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("==#" * 5, "Form Validated.")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return Response(form.cleaned_data)

        return Response({"msg": "Failed"})


def login(request):
    """
    Render the login page.
    """
    return render(request, "login.html")


def register(request):
    """
    Render the login page.
    """
    return render(request, "signup.html")


def jobTemp(request):
    """
    Render the login page.
    """
    return render(request, "jobapplicationformTemp.html")


def formTemp(request):
    """
    Render the login page.
    """
    return render(request, "formTemplate.html")


def meetCreatars(request):
    """
    Render the login page.
    """
    return render(request, "meetcreaters.html")


def jdTemp(request):
    """
    Render the login page.
    """
    return render(request, "JDTemplate.html")


def brandProTemp(request):
    """
    Render the login page.
    """
    return render(request, "brandprofileTemplate.html")


def creatARproTemp(request):
    """
    Render the login page.
    """
    print("==#" * 10, request.user.is_authenticated)
    return render(request, "creatARprofileTemplate.html", {"user": request.user})


def jobDetails(request):
    """
    Render the login page.
    """
    return render(request, "jobDetails.html")


def brandSettings(request):
    """
    Render the login page.
    """
    return render(request, "brandsSettings.html")


# Create your views here.
def landing_page(request):
    """
    Render the landing page.
    """

    # Get all podcasts
    podcasts = Podcast.objects.all()
    video_ids = [video_id_extractor(podcast.stream_link) for podcast in podcasts]
    podcasts_w_vid = zip(podcasts, video_ids)

    # Render view
    return render(request, "landing_page.html", {"podcasts": podcasts_w_vid})
