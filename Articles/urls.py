from django.urls import path
from Articles import views

urlpatterns = [
    path('', views.articles, name="home_page"),
]