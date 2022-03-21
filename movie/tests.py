from django.test import TestCase
from movie.models import Movie
from django.urls import reverse

# Create your tests here.
class MovieMethodTests(TestCase):

    def test_ensure_rating_are_positive(self):
        """
        Ensures the number of rating received for a Movie are positive or zero.
        """
        movie= Movie(title='test',rating=-1)
        movie.save()

        self.assertEqual((movie.rating>=0),True)

    def test_ensure_year_are_positive(self):
        """
        Ensures the number of year received for a Movie are positive or zero.
        """
        movie= Movie(title='test',year=-1)
        movie.save()

        self.assertEqual((movie.year>=0),True)

    def test_ensure_title_are_not_empty(self):
        """
        Ensures the title of movie received for a Movie are not empty string.
        """
        movie= Movie(title='')
        movie.save()

        self.assertEqual((len(movie.title)>0),True)
        self.assertEqual(movie.title, 'unknown movie')

    def test_slug_line_creation(self):
        """
        Checks to make sure that when a movie is created, an
        appropriate slug is created.
        Example: "Random Movie String" should be "random-movie-string".
        """
        movie = Movie(title='Random Movie String')
        movie.save()
        self.assertEqual(movie.slug, 'random-movie-string')

# helper function
def add_movie(title):
        # use default parameter
        movie = Movie.objects.get_or_create(title=title)[0]
        movie.save()
        return movie

# test for views
class MovieViewTests(TestCase):
    

    def test_movie_view_with_no_movies(self):
        """
        If no movies exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('movie:allmovies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<strong>There are no movies in the database yet.</strong>')
        self.assertQuerysetEqual(response.context['movies'], [])

    def test_movie_view_with_movies(self):
        """
        Checks whether movies are displayed correctly when present.
        """
        add_movie('Testing Movie 1')
        add_movie('Testing Movie 2')
        add_movie('Testing Movie 3')
        response = self.client.get(reverse('movie:allmovies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Testing Movie 1')
        self.assertContains(response, 'Testing Movie 2')
        self.assertContains(response, 'Testing Movie 3')
        num_movies = len(response.context['movies'])
        self.assertEquals(num_movies, 3)

