from django.contrib import admin
from .models import Announcement
from .models import Event
from .models import Resource

# Register your models here.
admin.site.register(Resource)
admin.site.register(Announcement)
admin.site.register(Event)