from django.urls import path
from . import views

urlpatterns  = [
    path('', views.request_list_create_view, name='request-list'),
    path('<int:pk>/', views.request_detail_view, name='request-detail'),
    path('<int:pk>/', views.request_update_view, name='request-update'),
    path('<int:pk>/', views.request_destroy_view, name='request-delete'),
    path('<int:pk>/messages/',views.messages_list_view, name='request_message_list'),
    path('<int:requestId>/messages/<int:pk>/',views.messages_detail_view, name='request_message_detail'),
    path('<int:requestId>/messages/<int:pk>/attachements/',views.attachement_list_create_view, name='request_message_attachement_list')
]