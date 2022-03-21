from django.test import TestCase

from django.urls import reverse
from forum.models import Post, PostReply
from user.models import User, UserProfile
from movie.models import Movie, Review, FavouriteList

# Create your tests here.

# helper function
def add_user(username, password, email):
    a = User.objects.get_or_create(username=username)[0]
    a.password = password
    a.email = email
    a.save()
    return a

def add_post(author, title, content):
    c = Post.objects.get_or_create(author=author)[0]
    c.title = title
    c.content = content
    c.save()
    return c

class ForumViewTests(TestCase):

    def test_forum_view_with_no_posts(self):
        """
        If no posts exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('forum:forum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<strong>There are no post present.</strong>')
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_post_view_with_posts(self):
        """
        Checks whether posts are displayed correctly when present.
        """
        user=add_user('test user1', '12345', 'test@email')
        add_post(user,'Testing 1','Testing1')

        user=add_user('test user2', '12345', 'test@email')
        add_post(user,'Testing 2','Testing2')

        user=add_user('test user3', '12345', 'test@email')
        add_post(user,'Testing 3','Testing3')
        

        response = self.client.get(reverse('forum:forum'))
        self.assertEqual(response.status_code, 200)

        num_postes = len(response.context['posts'])

        self.assertEquals(num_postes,3)