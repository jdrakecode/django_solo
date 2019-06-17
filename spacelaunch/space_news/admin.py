from django.contrib import admin

from .models import Launches, News

# Register your models here.
admin.site.register(Launches)
admin.site.register(News)