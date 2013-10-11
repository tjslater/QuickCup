from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import User, Industry, Location
from app.forms import Login_Form
import random


def login(request):
    data = {}
    if request.method == "POST":
        form = Login_Form(request.POST)
        print form
        if form.is_valid():
            print "form is valid"
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            headline = form.cleaned_data["headline"]
            linkedin = form.cleaned_data["linkedin"]
            picture_url = form.cleaned_data["picture_url"]
            location = form.cleaned_data["location"]
            industry = form.cleaned_data["industry"]
            latitude = 37.7533 + ((random.random() - .5) / 10)
            longitude = -122.4507 + ((random.random() - .5) / 10)
            profile_url = form.cleaned_data["profile_url"]
            user_exists = User.objects.filter(linkedin=linkedin).exists()
            industry = Industry.objects.get_or_create(name=industry)[0]
            location = Location.objects.get_or_create(name=location)[0]
            print "user_exists:", user_exists
            if not user_exists:
                profile = User(first_name=first_name, industry=industry, location=location,
                               last_name=last_name, headline=headline, linkedin=linkedin,
                               picture_url=picture_url, longitude=longitude,
                               latitude=latitude, profile_url=profile_url)
                profile.save()
            profile = User.objects.get(linkedin=linkedin)
            request.session['profile'] = profile
            return redirect('/feed')
        else:
            print "first else"
            form = Login_Form()
            profile = request.session.get('profile', False)
            print profile
            if profile:
                print profile
                return #redirect('/main')
            data['login_form'] = form  # DO NOT MOVE THIS

    else:
        print "second else"
        profile = request.session.get('profile', False)
    if profile:
        return redirect('/feed')
    else:
        form = Login_Form()
        # make_profile(form, request)

    form = Login_Form()
    data['login_form'] = form  # DO NOT MOVE THIS EITHER
    return render(request, "login_page.html", data)