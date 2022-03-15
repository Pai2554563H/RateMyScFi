from django.urls import path
from forum import views


app_name = 'forum'
urlpatterns = [path('', views.ForumView.as_view(), name='forum'),
]
