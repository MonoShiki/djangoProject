from django.shortcuts import render, redirect

from manga.models import Manga


def index(request):
    objects = Manga.objects.all()
    return render(request, 'main/index.html', {'objects': objects})
