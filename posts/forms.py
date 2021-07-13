from django.forms import ModelForm, fields

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
