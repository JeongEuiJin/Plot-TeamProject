# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 18:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_post_poster_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('seoul', '서울'), ('busan', '부산'), ('incheon', '인천'), ('daejeon', '대전'), ('daegu', '대구'), ('ulsan', '울산'), ('gwangju', '광주'), ('gyeonggi', '경기도'), ('gangwon', '강원도'), ('chungcheonnam', '충청남도'), ('chungcheonbuk', '충청북도'), ('gyeongsangnam', '경상남도'), ('gyeongsangbuk', '경상북도'), ('jeollanam', '전라남도'), ('jeollabuk', '전라북도'), ('jeju', '제주')], default='seoul', help_text='지역 선택', max_length=50),
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', through='post.PostLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together=set([('post', 'user')]),
        ),
    ]
