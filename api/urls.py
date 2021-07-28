from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('all_posts/', views.AllPosts.as_view(), name='allposts'),

]
