
from rest_framework import serializers
from posts.models import Post, Like, Comment

from django.contrib.auth import get_user_model
User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'message', 'image',
                  'created_at', 'likes', 'comments', 'group']

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_group(self, obj):
        if obj.group:
            return obj.group.name

    def get_comments(self, obj):
        return Comment.objects.filter(post=obj.id).count()
