from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True)
    link = models.URLField()

class BookReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.reviewer:
            self.reviewer = get_user_model().objects.get(pk=1) 
        super().save(*args, **kwargs)
        
class Poem(models.Model):
    poem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True)
    link = models.URLField()

class PoemReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    poem_id = models.ForeignKey(Poem, on_delete=models.CASCADE)
    review = models.TextField()
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.reviewer:
            self.reviewer = get_user_model().objects.get(pk=1) 
        super().save(*args, **kwargs)

class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to="story_covers/", blank=True)
    link = models.URLField()

class StoryReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    review = models.TextField()
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.reviewer:
            self.reviewer = get_user_model().objects.get(pk=1) 
        super().save(*args, **kwargs)

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to="article_covers/", blank=True)
    link = models.URLField()

class ArticleReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    review = models.TextField()
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.reviewer:
            self.reviewer = get_user_model().objects.get(pk=1) 
        super().save(*args, **kwargs)