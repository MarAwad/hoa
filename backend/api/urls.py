from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.api_home),
    path('requests/',include('contractrequests.urls')),
    path('tickets/',include('tickets.urls')),

]