from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from movie.forms import MovieForm
from movie.models import Movie
from django.conf import settings






# Create your views here.


def movielist(request):
    movie_list = Movie.objects.order_by('title')
    context_dict = {'movies': movie_list, 'MEDIA_URL':settings.MEDIA_URL}

    response = render(request, 'movie/allmovies.html', context=context_dict)

    return response

def singlemovie(request, singlemovie_name_slug):
    current_movie = Movie.objects.get(slug=singlemovie_name_slug)
    context_dict = {'movie': current_movie, 'MEDIA_URL':settings.MEDIA_URL}


    response = render(request, 'movie/singlemovie.html', context=context_dict)
    return response




def add_movie(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES or None)
        

        if form.is_valid():

            # if 'poster' in request.FILES:
            #     Movie.poster = request.FILES['poster']

            form.save(commit=True)
            return redirect('/movie/allmovies')
        else:
            print(form.errors)

    return render(request, 'movie/addmovie.html', {'form': form})
     