from django.contrib import admin
from movie.models import Movie


class movieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'rating', 'description')



# Register your models here.
admin.site.register(Movie, movieAdmin)



