from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'user/homepage.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'user/about.html', context=context_dict)
