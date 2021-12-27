from django.urls import path

# Views
from .views import index

urlpatterns = [
    path("", index, name="home"),
]
