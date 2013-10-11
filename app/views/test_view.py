from django.shortcuts import render
from linkedin import linkedin

def test(request):
    return render(request, 'index.html', {})