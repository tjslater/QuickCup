__author__ = 'Confucius'

from django.shortcuts import render


def meeting_confirmed(request):
    data = {'info': 'meeting confirmed!'}
    return render(request, 'meeting_confirmed_page.html', data)