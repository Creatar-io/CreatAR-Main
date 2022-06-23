from django.shortcuts import render

# Importing models
from core.models.podcast import Podcast

# Extract Video-ID from the video URL
video_id_extractor = lambda x: str(x)[str(x).rindex("=") + 1 : ]

# Create your views here.
def landing_page(request):
    """
    Render the landing page.
    """
    return render(request, "landing_page.html")

def login(request):
    '''
    Render the login page.
    '''
    return render(request, "login.html")

def register(request):
    '''
    Render the login page.
    '''
    return render(request, "signup.html")

def jobTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "jobapplicationformTemp.html")  

def formTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "formTemplate.html")  

def meetCreatars(request):
    '''
    Render the login page.
    '''
    return render(request, "meetcreaters.html")   

def jdTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "JDTemplate.html")

def brandProTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "brandprofileTemplate.html")

def creatARproTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "creatARprofileTemplate.html")

def jobDetails(request):
    '''
    Render the login page.
    '''
    return render(request, "jobDetails.html")

def brandSettings(request):
    '''
    Render the login page.
    '''
    return render(request, "brandsSettings.html")

def basicinfobrand(request):
    '''
    Render the login page.
    '''
    return render(request, "basicinforBrand.html")
        # Get all podcasts
    podcasts = Podcast.objects.all()
    video_ids = [video_id_extractor(podcast.stream_link) for podcast in podcasts]
    podcasts_w_vid = zip(podcasts, video_ids)

    # Render view
    return render(request, "landing_page.html", {"podcasts": podcasts_w_vid})
