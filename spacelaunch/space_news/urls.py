from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("news", views.news, name="news"),
    path("launch", views.launch, name="launch"),
    path("add_news", views.add_news, name="add_news"),
    path("add_launch", views.add_launch, name="add_launch"),
    path("delete", views.delete_news, name="delete_news"),
    path("delete_launch", views.delete_launch, name="delete_launch"),
    path("update_news/<int:id>", views.update_news, name="update_news"),
    path("update_launch/<int:id>", views.update_launch, name="update_launch"),
]
