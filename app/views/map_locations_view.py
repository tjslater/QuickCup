__author__ = 'Confucius'

from django.shortcuts import render
from app.models import User
from django.core import serializers

def map_locations(request):


    profiles = serializers.serialize("json", User.objects.all())

    data = {'profiles': profiles}
    return render(request, 'map_locations_page.html', data)
