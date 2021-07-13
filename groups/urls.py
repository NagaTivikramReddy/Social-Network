
from django.urls import path

from . import views
from posts import views as postviews

app_name = 'groups'

urlpatterns = [
    path('<slug>/', views.SingleGroup.as_view(), name='single'),
    path('<int:pk>/posts/', postviews.GroupPosts, name='groupposts'),
    path('', views.ListGroups.as_view(), name='all'),
    path('new', views.CreateGroup.as_view(), name='create'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave')
]
