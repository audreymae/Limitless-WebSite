from django.urls import path
from Logins import views

urlpatterns = [
    path('', views.logins, name="home_page"),
]