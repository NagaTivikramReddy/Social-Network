# Generated by Django 3.1.4 on 2021-07-12 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20210712_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='commented',
            field=models.ManyToManyField(blank=True, default=None, related_name='postcommented', to=settings.AUTH_USER_MODEL),
        ),
    ]