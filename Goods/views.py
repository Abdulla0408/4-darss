from django.shortcuts import render
from . import models


def banner(request):
    banners = models.Banner.objects.filter(is_active=True)[:5]
    context = {'banners': banners}
    return render(request, 'index.html', context)


def footer(request):
    footers = models.Footer.objects.all()
    context = {'footers': footers}
    return render(request, 'index.html', context)