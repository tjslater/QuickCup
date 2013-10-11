from django.shortcuts import render
from app.forms import User_Search


def user_search(request):
    return render(request, "user_search_page.html", {})