from django.urls import path
from movie import views


app_name = 'movie'
urlpatterns = [
    path('allmovies', views.movielist, name='allmovies'),
    path('addmovie', views.add_movie, name='addmovie'),
    path('singlemovie/<slug:singlemovie_name_slug>/', views.singlemovie, name='singlemovie'),

]
