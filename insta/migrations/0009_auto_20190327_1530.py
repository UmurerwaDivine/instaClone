# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0008_auto_20190327_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('liked', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='upload_date',
            new_name='pub_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='image',
            name='likess',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='s', upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='insta.Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Image'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
