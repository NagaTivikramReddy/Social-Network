from django.db import models
from django.db.models.query import ValuesListIterable
from django.urls import reverse
from django.conf import settings

from groups.models import Group, GroupMember

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='userposts',
                             on_delete=models.CASCADE)
    message = models.TextField()
    #message_html = models.TextField(editable=False)
    image = models.ImageField(upload_to='posts/images', blank=True, default='')
    created_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(
        Group, related_name='groupposts', on_delete=models.CASCADE)
    liked = models.ManyToManyField(User, default=None, blank=True)
    # commented = models.ManyToManyField(
    #     User, related_name='postcommented', default=None, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        #message_html = misaka.html(self.message)
        super().save(*args, *kwargs)

    @property
    def NumeberOfLikes(self):
        return self.objects.all().count()

    # @property
    # def NumberofComments(self):
    #     return self.objects.all().count()

    class Meta:
        #ordering = ['-created_at']
        unique_together = ['user', 'message']

    def get_absolute_url(self):
        return reverse('posts:single',  kwargs={'username': self.user.username, 'pk': self.pk})


'''The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name'''
Like_Choices = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='liked_user')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="liked_post")
    value = models.CharField(choices=Like_Choices,
                             max_length=10, default='Like')

    def __str__(self):
        return self.user


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='commentpost', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commented_user')
    comment = models.TextField()

    def __str__(self):
        return self.comment
