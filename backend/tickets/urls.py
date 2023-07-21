from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ticket_list_create_view),
    path('<int:pk>/',views.ticket_detail_view),
    path('<int:pk>/messages/',views.messages_list_create_view),
    path('<int:ticket>/messages/<int:pk>/',views.message_detail_view),
    path('<int:ticket>/messages/<int:message>/attachements/',views.attachement_list_create_view),
    path('<int:ticket>/attachements/',views.contract_attachement_list_view),
]
