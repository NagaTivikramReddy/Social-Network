from django.shortcuts import render
from rest_framework import generics, permissions
from posts.models import Post
from .serializers import PostSerializer


class AllPosts(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    permisssion_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all()
