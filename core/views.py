from django.shortcuts import render

from .models import Restaurant, Rating, Sale

def index(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}

    return render(request, 'index.html', context)
