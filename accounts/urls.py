from django.urls import path

# Views
from .views import profile_view


urlpatterns = [
    path("profile/", profile_view, name="profile"),
]
