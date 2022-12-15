from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from app.models import *
from django.db.models.functions import Length
def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.filter(name__startswith='m')
    LWO=Webpage.objects.filter(name__endswith='a')
    LWO=Webpage.objects.filter(name__contains='s')
    LWO=Webpage.objects.filter(name__in=('Meghana','MSD'))
    LWO=Webpage.objects.filter(name__regex='^M\w{6}')
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(topic_name='cricket') & Q(name__startswith='M'))
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(topic_name='Boxing') | Q(url__endswith='in'))
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LAO=Access_Records.objects.all()
    LAO=Access_Records.objects.filter(date='2022-10-22')
    LAO=Access_Records.objects.filter(date__year='2022')
    LAO=Access_Records.objects.filter(date__month='12')  
    LAO=Access_Records.objects.filter(date__day='3') 
    LAO=Access_Records.objects.filter(date__gte='2021-8-3')
    LAO=Access_Records.objects.filter(date__lte='2022-12-12')
    LAO=Access_Records.objects.filter(date__year__gte='2022')
    d={'LAO':LAO}
    return render(request,'display_access.html',d)
