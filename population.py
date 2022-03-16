import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'RateMyScFi.settings')

import django

django.setup()
from forum.models import Post, PostReply


def populate():
    # posts = [
    #     {'title': 'Official Python Tutorial',
    #      'author': 'admin',
    #      'content': ''},
    #     {'title': 'How to Think like a Computer Scientist',
    #      'url': 'http://www.greenteapress.com/thinkpython/'},
    #     {'title': 'Learn Python in 10 Minutes',
    #      'url': 'http://www.korokithakis.net/tutorials/python/'}]
    pass


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
