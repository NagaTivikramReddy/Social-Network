from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'api'


urlpatterns = [
    path('all_posts/', views.AllPosts.as_view(), name='allposts'),
    path('example/', views.Example.as_view(), name='example'),
    # path('login/', obtain_auth_token, name='login'),
    # path('user/', views.LoginView.as_view(), name='user'),
    path('jwttoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwttoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('xxxx/', views.LoginView.as_view(), name='xxx')

]
