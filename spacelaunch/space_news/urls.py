from django.urls import path

from .views import index, news, launch

urlpatterns = [
    path("", index, name="home"),
    path("news", news, name="news"),
    path("launch", launch, name="launch")
]
