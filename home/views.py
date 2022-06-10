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
    # Get all podcasts
    podcasts = Podcast.objects.all()
    video_ids = [video_id_extractor(podcast.stream_link) for podcast in podcasts]
    podcasts_w_vid = zip(podcasts, video_ids)

    # Render view
    return render(request, "landing_page.html", {"podcasts": podcasts_w_vid})
