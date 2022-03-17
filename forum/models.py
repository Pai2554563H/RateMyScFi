from django.db import models
from user.models import User
from movie.models import Movie


class Forum(models.Model):
    name = models.CharField(max_length=128)


class Post(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, )
    title = models.TextField(default='')
    date = models.DateField(auto_now=False, auto_now_add=True)
    content = models.TextField()
    # topic = models.TextField()

    def __str__(self):
        return self.title


class PostReply(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, )
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, )
    date = models.DateField(auto_now=False, auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content
