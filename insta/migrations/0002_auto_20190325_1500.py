# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 13:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
