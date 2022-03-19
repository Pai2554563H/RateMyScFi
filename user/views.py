from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from user.froms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.conf import settings

# load model
from movie.models import Movie


def homepage(request):
    
    context_dict={}

    # top 10 by rating
    movie_list = Movie.objects.order_by('title')
    top_10 = Movie.objects.order_by('-rating')[:10]

    context_dict['movies'] = movie_list
    context_dict['top_10'] = top_10
    context_dict['MEDIA_URL']=settings.MEDIA_URL


    return render(request, 'user/homepage.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'user/about.html', context=context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'user/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('homepage'))
            else:
                return HttpResponse("Your Rate My Sc-Fi account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'user/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('user:login'))


class UserProfileView(TemplateView):
    template_name = 'user/user_page.html'

    def get_context_data(self, **kwargs):
        print(self.request.user)
