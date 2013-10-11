from django.shortcuts import render, redirect
from app.forms import Profile_Form
from app.models.users_model import User
from app.models.industry_model import Industry



__author__ = 'Confucius'


def profile(request):
    data = {}
    user = request.session.get('profile')
    user_data = User.objects.get(linkedin=user.linkedin)
    form = Profile_Form(request.POST)
    if request.method == "POST":
        print form
        if form.is_valid():
            print "form is valid"
            user_data.first_name = form.cleaned_data["first_name"]
            user_data.last_name = form.cleaned_data["last_name"]
            user_data.headline = form.cleaned_data["headline"]
            user_data.experience = form.cleaned_data["experience"]
            user_data.age = form.cleaned_data["age"]
            user_data.last_name = form.cleaned_data["last_name"]
            user_data.availability = form.cleaned_data["availability"]
            print user_data.first_name
            user_data.save()
            print user_data.first_name
            request.session['profile'] = user_data
            return redirect('/feed')
        else:
            print "didn't work"
            print user_data.first_name
            print user_data.last_name


    data = {"user": user, "profile_form": form}
    return render(request, 'profile_page.html', data)