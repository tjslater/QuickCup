from app.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def feed(request):
    user_list = User.objects.all() # user_list = serializers.serialize("json", User.objects.all())
    profile = request.session.get('profile', return_to_login())
    data = {'users': user_list, 'profile': profile}
    return render(request, 'feed_page.html', data)

def convert(obj):
    if isinstance(obj, dict):
        return {convert(key): convert(value) for key, value in obj.iteritems()}
    elif isinstance(obj, list):
        return [convert(element) for element in obj]
    elif isinstance(obj, unicode):
        return obj.encode('utf-8')
    else:
        return obj

def return_to_login():
    return redirect('/')
    pass