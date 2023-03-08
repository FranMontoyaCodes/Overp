from django.urls import path
from overpinfo.views import (
    overp_info,)

urlpatterns = [
    path('overpinfo/', overp_info, name="overp"),
]
