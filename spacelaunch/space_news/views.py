from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "space_news/home.html")

def news(request):
    return render(request, "space_news/news_archive.html")

def launch(request):
    return render(request, "space_news/launch_archive.html")

def add_news(request):
    return render(request, "space_news/add_news.html")

def add_launch(request):
    return render(request, "space_news/add_launch.html")