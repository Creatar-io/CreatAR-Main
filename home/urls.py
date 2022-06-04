from django.urls import path

# importing views from views..py
from .views import (
    landing_page,
)

urlpatterns = [
    path("", landing_page),
]
