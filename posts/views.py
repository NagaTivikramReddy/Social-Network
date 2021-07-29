from groups.models import Group, GroupMember
from django.db import models
from .forms import *
from .models import Like, Post
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.contrib import messages

from django.http import Http404
from django.urls import reverse_lazy

from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, ListView):
    model = Post
    select_related = ('user', 'group')

    def get_queryset(self):
        print(self.kwargs)
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        self.temp = Post.objects.select_related(
            'user').filter(user__username=self.kwargs.get('username'))
        return self.temp

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.kwargs.get('username')
        return context


class UserPostDetails(LoginRequiredMixin, SelectRelatedMixin, DetailView):
    model = Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = Post
    fields = ('message', 'image', 'group')

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)


def GroupPosts(request, pk):
    grpposts = Post.objects.filter(group__id=pk)
    return render(request, 'posts/group_posts.html', {'groupposts': grpposts})


def PostLike(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    if user in post.liked.all():
        post.liked.remove(user)
    else:
        post.liked.add(user)

    like, created = Like.objects.get_or_create(user=user, post_id=post.pk)

    if not created:
        if like.value == "Like":
            like.value = "Unlike"
        else:
            like.value = "Like"

    like.save()
    post.save()

    return redirect('home')


def PostComment(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.user = user
            obj.save()

            return redirect('home')
    else:
        form = CommentForm()

    return render(request, 'posts/comment_form.html', {'form': form})


def CommentDetails(request, pk):
    post = get_object_or_404(Post, pk=pk)

    commentedpost = Post.objects.prefetch_related(
        'commentpost').get(id__exact=post.pk)

    post_comments = commentedpost.commentpost.all()

    return render(request, 'posts/post_comments.html', {'post_comments': post_comments, 'post': post})


class DeleteComment(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Comment
    select_related = ('post',)
    success_url = reverse_lazy('posts:all')
