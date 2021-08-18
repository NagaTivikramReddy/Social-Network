import jwt
from rest_framework.exceptions import AuthenticationFailed
import datetime
from django.db.models.query import QuerySet
from groups.models import Group
from django.shortcuts import render
from rest_framework import generics, permissions
from posts.models import Post
from .serializers import PostSerializer, ExampleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


class AllPosts(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    permisssion_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TakenAuthentication]

    def get_queryset(self):
        return Post.objects.all()


class Example(generics.ListAPIView):
    model = Group
    serializer_class = ExampleSerializer

    def get_queryset(self):
        print(self.request.query_params)
        return Group.objects.all()


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
