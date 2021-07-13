from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('like/<int:pk>/', views.PostLike, name='postlike'),
    path('comment/<int:pk>/', views.PostComment, name='postcomment'),
    path('viewcomments/<int:pk>/',
         views.CommentDetails, name='commentdetails'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.UserPostDetails.as_view(), name='single'),
    path('delete/<pk>', views.DeletePost.as_view(), name='delete'),
    path('comment/delete/<int:pk>/',
         views.DeleteComment.as_view(), name='deletecomment'),

]
