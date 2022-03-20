import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'RateMyScFi.settings')

import django

django.setup()
from forum.models import Post, PostReply
from user.models import User, UserProfile
from movie.models import Movie, Review, FavouriteList


def populate():
    users = {'Yiqi Li': {'username': 'yiqiL',
                         'password': 'pbkdf2_sha256$120000$F7YcLpLQIhZd$B/2FmSqsn7DUQVXwmZ0p5skGDiUcMUE/3RjK5XDzrWw=',
                         'email': '2640204L@student.gla.ac.uk',
                         'picture': 'profile_images/YIQILI.jpeg'},
             'Valborg Johannesen': {'username': 'valborgJ',
                                    'password': 'pbkdf2_sha256$120000$F7YcLpLQIhZd$B/2FmSqsn7DUQVXwmZ0p5skGDiUcMUE/3RjK5XDzrWw=',
                                    'email': '2328244j@student.gla.ac.uk',
                                    'picture': 'profile_images/ValborgJohannesen.jpeg'},
             'Pai Huang': {'username': 'paiH',
                           'password': 'pbkdf2_sha256$120000$F7YcLpLQIhZd$B/2FmSqsn7DUQVXwmZ0p5skGDiUcMUE/3RjK5XDzrWw=',
                           'email': '2554563h@student.gla.ac.uk',
                           'picture': 'profile_images/PaiHuang.jpeg'},
             'Dougie Price': {'username': 'dougieP',
                              'password': 'pbkdf2_sha256$120000$F7YcLpLQIhZd$B/2FmSqsn7DUQVXwmZ0p5skGDiUcMUE/3RjK5XDzrWw=',
                              'email': '2250864p@student.gla.ac.uk',
                              'picture': 'profile_images/DougiePrice.jpeg'},
             'Hanze Li': {'username': 'hanzeL',
                          'password': 'pbkdf2_sha256$120000$F7YcLpLQIhZd$B/2FmSqsn7DUQVXwmZ0p5skGDiUcMUE/3RjK5XDzrWw=',
                          'email': '22690422l@student.gla.ac.uk',
                          'picture': 'profile_images/HanzeLi.jpeg'},
             }

    reply1 = [{'author_name': 'dougieP',
               'content': 'Love it.'
               },
              {'author_name': 'hanzeL',
               'content': 'Best Batman ever.'
               }
              ]

    reply2 = [{'author_name': 'paiH',
               'content': 'It\'s a classic.'
               },
              {'author_name': 'yiqiL',
               'content': 'I\'m going to re-watch that tonight.'
               }
              ]

    posts = {'post1': {'title': 'Like batman',
                       'content': 'Just watched it. Perhaps not the definitive version, but definitely a worthwhile take',
                       'author_name': 'yiqiL',
                       'reply': reply1},
             'post2': {'title': 'I love the old batman more',
                       'content': 'Anybody remember Christian Bale?',
                       'author_name': 'valborgJ',
                       'reply': reply2},
             }

    Review1 = [{'author_name': 'dougieP',
                'rating': '8',
                'content': 'Love it.'
                },
               {'author_name': 'valborgJ',
                'rating': '9',
                'content': 'recommend it.'
                },
               {'author_name': 'paiH',
                'rating': '9',
                'content': 'Love it.'
                },
               ]

    Review2 = [{'author_name': 'yiqiL',
                'rating': '5',
                'content': 'almost fell asleep in the cinema.'
                },
               {'author_name': 'hanzeL',
                'rating': '6',
                'content': 'boring.'
                }
               ]

    movies = {'Batman': {'title': 'The Batman',
                         'description': 'When the Riddler, a sadistic serial killer, begins murdering key political figures in Gotham, Batman is forced to investigate the city\'s hidden corruption and question his family\'s involvement.',
                         'director': 'Matt Reeves',
                         'year':2022,
                         'poster': 'posters/batman.jpg',
                         'review': Review1},
              'venom': {'title': 'Venom: Let There Be Carnage',
                        'description': 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, who becomes the host of the symbiote Carnage and escapes prison after a failed execution.',
                        'director': 'Andy Serkis',
                        'year':2021,
                        'poster': 'posters/venom.jpg',
                        'review': Review2},
              }

    for user, user_data in users.items():
        a = add_user(user_data['username'], user_data['password'], user_data['email'])
        b = add_userProfile(a, user_data['picture'])

    for post, post_data in posts.items():
        c = add_post(find_user(post_data['author_name']), post_data['title'], post_data['content'])
        for r in post_data['reply']:
            add_reply(c, find_user(r['author_name']), r['content'])

    for movie, movie_data in movies.items():
        e = add_movie(movie_data['title'], movie_data['year'], movie_data['director'], movie_data['description'], movie_data['poster'])
        for review in movie_data['review']:
            add_review(e, find_user(review['author_name']), review['rating'], review['content'])


def find_user(username):
    user = User.objects.get_or_create(username=username)[0]
    return user


def add_user(username, password, email):
    a = User.objects.get_or_create(username=username)[0]
    a.password = password
    a.email = email
    a.save()
    return a


def add_userProfile(user, picture):
    b = UserProfile.objects.get_or_create(user=user)[0]
    b.picture = picture
    b.save()
    return b


def add_post(author, title, content):
    c = Post.objects.get_or_create(author=author)[0]
    c.title = title
    c.content = content
    c.save()
    return c


def add_reply(post, author, content):
    d = PostReply.objects.get_or_create(author=author, post=post)[0]
    d.content = content
    d.save()
    return d


def add_movie(title, year, director, description, poster):
    e = Movie.objects.get_or_create(title=title, year=year)[0]
    e.director = director
    e.description = description
    e.poster = poster
    e.save()
    return e


def add_review(movie, author, rating, content):
    f = Review.objects.get_or_create(movie=movie, user=author)[0]
    f.rating = rating
    f.content = content
    f.save()
    return f


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    print('Finished!')
