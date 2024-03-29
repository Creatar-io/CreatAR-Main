from django.urls import path

# importing views from views..py
from .views import (
    landing_page,
    login,
    register,
    jobTemp,
    formTemp,
    meetCreatars,
    jdTemp,
    brandProTemp,
    creatARproTemp,
    jobDetails,
    brandSettings,
    basicinfobrand,
    OrganisationRegistrationHandler,
    OrganisationModeratorRegistrationHandler,
)

urlpatterns = [
    path("", landing_page),
    path("login", login),
    path("register", register),
    path("jobTemp", jobTemp),
    path("formTemp", formTemp),
    path("meetCreatars", meetCreatars),
    path("jdTemp", jdTemp),
    path("brandProTemp", brandProTemp),
    path("creatARproTemp", creatARproTemp),
    path("jobDetails", jobDetails),
    path("brandSettings", brandSettings),
    path("basicinfobrand", basicinfobrand),

    path("register/org", OrganisationRegistrationHandler.as_view()),
    path("register/orgmoderator", OrganisationModeratorRegistrationHandler.as_view()),
]
