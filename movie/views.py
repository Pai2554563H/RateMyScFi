from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from movie.models import Movie





# Create your views here.


def movielist(request):
    movie_list = Movie.objects.order_by('title')
    context_dict = {'movies': movie_list}

    response = render(request, 'movie/allmovies.html', context=context_dict)

    return response

def singlemovie(request, singlemovie_name_slug):
    current_movie = Movie.objects.get(slug=singlemovie_name_slug)
    context_dict = {'movie': current_movie}


    response = render(request, 'movie/singlemovie.html', context=context_dict)
    return response




# @login_required
def add_movie(request):
    response = render(request, 'movie/addmovie.html')
    return response