from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("news", views.news, name="news"),
    path("launch", views.launch, name="launch"),
    path("add_news", views.add_news, name="add_news"),
    path("add_launch", views.add_launch, name="add_launch"),
    path("delete", views.delete_news, name="delete_news"),
]
