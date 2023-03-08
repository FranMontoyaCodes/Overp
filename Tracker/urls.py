from django.urls import path
from Tracker.views import (
    Tracker,)

urlpatterns = [
    path('Tracker/', Tracker, name="Tracker"),
]
