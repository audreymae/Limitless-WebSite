from django.urls import path
from Meals import views

urlpatterns = [
    path('', views.meals, name="home_page"),
]