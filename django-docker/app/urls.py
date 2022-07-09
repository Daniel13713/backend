from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="app-home"),
    path('user/', views.user, name="app-user"),
    path('questions/', views.questions, name="app-questions"),
]
