from django.shortcuts import render
from .models import *
def homepage_view(request):
    context = {}
    last_home = HomePageContent.objects.last()

    context['contents'] = last_home.home_content.all()

    return render(request, 'index.html', context)
