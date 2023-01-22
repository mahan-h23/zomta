from django.shortcuts import render


def homepage_view(request):
    context = {}

    return render(request, 'index.html', context)
