from django.http import HttpResponse
from django.shortcuts import render





# Create your views here.


def movie(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'movie/allmovies.html', context=context_dict)