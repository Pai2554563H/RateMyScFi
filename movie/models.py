from django.db import models
from user.models import User
from django.template.defaultfilters import slugify


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(default=2000)
    director = models.CharField(max_length=128)
    rating = models.FloatField(default=0)
    description = models.TextField(default="")
    slug = models.SlugField(default="")


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, )
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, )
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now=False, auto_now_add=True)
    content = models.TextField()


class FavouriteList(models.Model):
    title = models.CharField(max_length=128)
    movie = models.ManyToManyField('Movie')
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, )


