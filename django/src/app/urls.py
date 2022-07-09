
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="api-home"),
    path('user/', views.user, name="api-user"),
]
