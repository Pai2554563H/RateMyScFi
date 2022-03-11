from django.http import HttpResponse
from django.shortcuts import render

from movie.models import Movie





# Create your views here.


def movie(request):

    movie_list = Movie.objects.order_by('-title')

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['movies'] = movie_list

    response = render(request, 'movie/allmovies.html', context=context_dict)

    return response


# def show_movies(request, movie_name_slug):

# @login_required
# def add_movie()