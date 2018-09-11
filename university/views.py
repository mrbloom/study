from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {'hello': 'world',
            'title': 'My Univer',
            'text': 'variable text value'}
    return render(request, 'university/index.html', data)
    # return HttpResponse("out")