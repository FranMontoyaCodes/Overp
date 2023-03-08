from django.urls import path
from Goals.views import (
    Goals,)

urlpatterns = [
    path('Goals/', Goals, name="Goals"),
]
