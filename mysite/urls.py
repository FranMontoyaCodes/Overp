"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from personal.views import (
	home_screen_view,)

from account.views import (
	registration_view,
    login_view,
    logout_view,
    account_view,
    must_authenticate_view,


	)
from overpinfo.views import (
    overp_info,)
from Tracker.views import (
    Tracker,)
from Goals.views import (
    Goals,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('logout/', logout_view, name="logout"),
    path('overpinfo/', overp_info, name="overp"),
    path('', home_screen_view, name="home"),
    path('Tracker/', Tracker, name="Tracker"),
    path('Goals/', Goals, name="Goals"),
   


    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    
]

