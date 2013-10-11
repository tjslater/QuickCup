from django.contrib.sessions.models import Session
from django.core import serializers
from django.shortcuts import render
from app.models.users_model import User
import requests
import pusher

__author__ = 'Confucius'


def send_invite(request, recipient):
    recipient = User.objects.get(linkedin=recipient)
    request.session['recipient'] = recipient
    sender = request.session.get('profile', 'no profile')
    # sender = serializers.serialize('json', sender)
    data = {"sender": sender, "recipient": recipient}
    return render(request, "send_invite_page.html", data)