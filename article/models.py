from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import auth

# Create your models here.
from django.http import request


class Article(models.Model):
    class META():
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title

class Comments(models.Model):
    class META():
        db_table = 'comments'

    comments_date = models.DateTimeField(default=datetime.now())
    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
