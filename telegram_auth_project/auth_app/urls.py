
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('check_auth_status/', views.check_auth_status, name='check_auth_status'),
]
