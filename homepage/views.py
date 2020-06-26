from django.shortcuts import render
from .models import Announcement
from .models import Event
from .models import Resource
# Create your views here.

def index(request):

    A1 = Announcement.objects.all()
    A2 = Event.objects.all()
    A3 = Resource.objects.all()

    year_list = []

    for a in A2.all():
        year_list.append(a.date_time.date().year)

    dicts = {}
    # keys = range(4)
    # values = ["Hi", "I", "am", "John"]
    # for i in keys:
    #         dicts[i] = values[i]  
    # print(dicts)

    t = []
    for tag in A3.all():
        t1 = tag.tags
        t2 = t1.split(" ")
        for i in t2:
            t = [tag.resource,tag.url_title]
            if i in dicts.keys():
                dicts[i].append(tag.resource)
                dicts[i].append(tag.url_title)
            else:
                dicts[i] = t
    

    d1 = {}
    lst = []
    for tag in A3.all():
        t1 = tag.tags
        t2 = t1.split(" ")
        for i in t2:
            t = [tag.resource,tag.url_title]
            if i in d1.keys():
                d1[i].append(tag.resource)
                d1[i].append(tag.url_title)
            else:
                d1[i] = t
    print(lst)
    


    #print(year_list) 
    
    return render(request, "index.html" , {'A1': A1 , 'A2' : A2 , 'year_list':year_list , 'A3': A3 ,'data': sorted(dicts.items())})

def allbuttons(request):

    if request.POST.get("events"):
        print("\n\nIn function Events")
        A2 = Event.objects.all()
        return render(request, "events.html" , {'A2': A2})

    if request.POST.get('resources'):
        print("\n\nIn function resources")
        A3 = Resource.objects.all()

        return render(request, "resources.html" , {'A3': A3})
    else:
        return render(request,"index.html")

def events(request):
    
     #if request.POST.get('events'):
        A2 = Event.objects.all()
        
        return render(request, "events.html" , {'A2': A2})

def resources(request): 
       
    #if request.POST.get('resources'):
        #A3 = Resources.objects.all()

        return render(request, "resources.html")# , {'A3': A3})