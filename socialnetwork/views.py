from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

from posts.models import Post
from groups.models import Group


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(ListView):
    model = Post
    template_name = 'index.html'
