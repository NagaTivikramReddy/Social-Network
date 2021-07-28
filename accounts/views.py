from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.contrib import messages
from . import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from braces.views import SelectRelatedMixin

from posts.models import Post
from groups.models import GroupMember

User = get_user_model()


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileDetails(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/customuser_detail.html'

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            self.user_posts = User.objects.prefetch_related(
                'userposts').get(username__iexact=self.kwargs.get('pk'))
            queryset = queryset  # TODO
            self.user_groups = User.objects.prefetch_related(
                'usergroups').get(username__iexact=self.kwargs.get('pk'))
            self.clicked_user = User.objects.get(
                username__iexact=self.kwargs.get('pk'))

        except User.DoesNotExist:
            raise ObjectDoesNotExist("Object doesn't exist")
        else:
            return self.user_posts.userposts.all(), self.user_groups.usergroups.all(), self.clicked_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = self.user_posts.userposts.all()
        context['user_groups'] = self.user_groups.usergroups.all()
        context['clicked_user'] = self.clicked_user
        return context
