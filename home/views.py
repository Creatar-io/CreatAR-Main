from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


# Importing models
from core.models.podcast import Podcast

# Extract Video-ID from the video URL
video_id_extractor = lambda x: str(x)[str(x).rindex("=") + 1 :]

# Importing forms
from core.froms import OrganisationForm, OrganisationModeratorForm

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
    return render(request, "creatARprofileTemplate.html")


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

def basicinfobrand(request):
    '''
    Render the login page.
    '''
    return render(request, "basicinforBrand.html")
        # Get all podcasts

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


def register_organisation_moderator(request):
    """
    This from collects organisation moderator POC details
    """
    user_email = None
    if request.user.is_authenticated:
        user_email = request.user.email

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = OrganisationModeratorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return {"msg": "Hello"}

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrganisationModeratorForm()

    return render(
        request,
        "register_organisation_moderator.html",
        {"form": form, "v_email": user_email},
    )
