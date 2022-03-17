from mimetypes import init
from django import forms
from movie.models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Title of movie")
    year = forms.IntegerField(initial=2000, help_text="Year of release")
    director = forms.CharField(max_length=128, help_text="Director")
    rating = forms.FloatField(initial=0, help_text="Movie rating")
    description = forms.CharField(widget=forms.Textarea, help_text="Add a synopsis ")
    poster = forms.ImageField(help_text="Add a poster", required=False)
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Movie
        fields = ('title', 'year', 'director', 'rating', 'description', 'poster', 'slug')