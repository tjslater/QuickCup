from django import forms


class Login_Form(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    headline = forms.CharField(max_length=128)
    industry = forms.CharField(max_length=64)
    linkedin = forms.CharField(max_length=128)
    picture_url = forms.CharField(max_length=128)
    location = forms.CharField(max_length=128)
    latitude = forms.CharField(max_length=64)
    longitude = forms.CharField(max_length=64)
    profile_url = forms.CharField(max_length=128)

class Profile_Form(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    headline = forms.CharField(max_length=128)
    experience = forms.CharField(max_length=4)
    age = forms.CharField(max_length=4)
    availability = forms.CharField(max_length=20)

class User_Search(forms.Form):
    search_field = forms.CharField(max_length=64)