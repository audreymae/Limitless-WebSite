from django.urls import path
from Workouts import views

urlpatterns = [
    path('', views.workout, name="home_page"),
]