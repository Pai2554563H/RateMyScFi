from django.urls import path
from forum import views
from forum import models


app_name = 'forum'
urlpatterns = [path('', views.ForumView.as_view(), name='forum'),
               path('<int:post_id>/', views.PostView.as_view(), name='show_post'),
               path('add_post/', views.AddPostView.as_view(), name='add_post'),
               path('<int:post_id>/add_reply/', views.AddReplyView.as_view(), name='add_reply'),
]
