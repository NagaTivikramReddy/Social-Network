from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

from posts.models import Post


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(ListView):
    model = Post
    template_name = 'index.html'
