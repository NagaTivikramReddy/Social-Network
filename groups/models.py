from django import template
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def create_default_group(self):
        self.name = "Public"
        self.description = "Public Group"
        self.save()

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(
        Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='usergroups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
