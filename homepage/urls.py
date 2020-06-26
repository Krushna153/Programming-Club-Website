from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from homepage import views


urlpatterns = [

    path("", views.index, name="index"),
    path("index1", views.index, name="index"),
    path("events", views.events, name="events"),
    path("allbuttons", views.allbuttons, name="option"),
    path("resources", views.resources, name="resources"),
    path('admin/', admin.site.urls),

]