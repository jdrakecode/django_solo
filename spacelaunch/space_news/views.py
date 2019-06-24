from django.shortcuts import render, redirect

from .models import Launches, News

from datetime import datetime

# Create your views here.
def index(request):
    my_news = News.objects.all()
    if len(my_news) > 1:
        my_news = my_news[::-1]
    multi_launch = Launches.objects.all()
    # multi_launch = sorted(multi_launch, key=lambda x: datetime.strptime(x["date"], "%m/%d/%y %H:%M"))
    if len(multi_launch) > 2:
        multi_launch = multi_launch[::-1]
    
    context = {
        "other_launches": multi_launch[0:3],
        "news": my_news[0:2],
    }
    return render(request, "space_news/home.html", context=context)

def news(request):
    my_news = News.objects.all()
    if len(my_news) > 1:
        my_news = my_news[::-1]

    context = {
        "news": my_news
    }
    return render(request, "space_news/news_archive.html", context=context)

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
    if request.method == "POST":
        new_news = News(date=request.POST["date"], name=request.POST["name"], info=request.POST["info"])
        new_news.save()
        return redirect("news")
    return render(request, "space_news/add_news.html")

def add_launch(request):
    if request.method == "POST":
        new_launch = Launches(date=request.POST["date"], name=request.POST["name"], payload=request.POST["payload"], time=request.POST["time"], site=request.POST["site"], description=request.POST["description"])
        new_launch.save()
        return redirect("launch")
    return render(request, "space_news/add_launch.html")

def delete_news(request):
    if request.method == "POST":
        to_delete = News.objects.get(id=request.POST["id"])
        to_delete.delete()
        return redirect("news")
    return redirect("news")

def delete_launch(request):
    if request.method == "POST":
        to_delete = Launches.objects.get(id=request.POST["id"])
        to_delete.delete()
        return redirect("launch")
    return redirect("launch")

def update_news(request, id):
    to_update = News.objects.get(id=id)
    if request.method == "POST":
        for key, value in request.POST.items():
            if value and key != "csrfauthenticationtoken":
                setattr(to_update, key, value)
                to_update.save()
        return redirect("news")
    context = {
        "id": id,
        "update": to_update
    }
    return render(request, "space_news/update_news.html", context=context)

def update_launch(request, id):
    to_update = Launches.objects.get(id=id)
    if request.method == "POST":
        for key, value in request.POST.items():
            if value and key != "csrfauthenticationtoken":
                setattr(to_update, key, value)
                to_update.save()
        return redirect("launch")
    context = {
        "id": id,
        "update": to_update
    }
    return render(request, "space_news/update_launch.html", context=context)
