
from groups.models import Group
from django.db import models
from rest_framework import serializers
from posts.models import Post, Like, Comment
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class ExampleSerializer(serializers.ModelSerializer):
    groupposts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'groupposts']


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


# class UserSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = '__all__'
