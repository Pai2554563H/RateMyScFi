from django.urls import path
from forum import views
from forum import models


app_name = 'forum'
urlpatterns = [path('', views.ForumView.as_view(), name='forum'),
               path('<int:post_id>/', views.PostView.as_view(), name='show_post')
]
