from django.shortcuts import render, redirect

from .models import Launches

from datetime import datetime

# Create your views here.
def index(request):
    multi_launch = Launches.objects.all()
    # multi_launch = sorted(multi_launch, key=lambda x: datetime.strptime(x["date"], "%m/%d/%y %H:%M"))
    if len(multi_launch) > 2:
        multi_launch = multi_launch[::-1]
    
    context = {
        "other_launches": multi_launch[0:2]
        # "other_launches": multi_launch
    }
    return render(request, "space_news/home.html", context=context)

def news(request):
    # my_news = News.objects.all()
    return render(request, "space_news/news_archive.html")

def launch(request):
    multi_launch = Launches.objects.all()
    # print("Launches:", len(multi_launch))
    if len(multi_launch) > 2:
        multi_launch = multi_launch[::-1]
    
    context = {
        "other_launches": multi_launch
    }
    return render(request, "space_news/launch_archive.html", context=context)

def add_news(request):
    return render(request, "space_news/add_news.html")

def add_launch(request):
    if request.method == "POST":
        new_launch = Launches(date=request.POST["date"], name=request.POST["name"], payload=request.POST["payload"], time=request.POST["time"], site=request.POST["site"], description=request.POST["description"])
        new_launch.save()
        return redirect("add_launch")
    return render(request, "space_news/add_launch.html")

