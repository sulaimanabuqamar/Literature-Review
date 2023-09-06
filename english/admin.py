from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book, BookReview, Poem, PoemReview, Story, StoryReview, Article, ArticleReview

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'cover', 'book_id']
    search_fields = ['title', 'book_id']

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'book_id', 'review', 'rating', 'reviewer']
    search_fields = ['review_id', 'book_id', 'review', 'rating', 'reviewer'] 
 
class PoemAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'cover', 'poem_id']
    search_fields = ['title', 'poem_id']

class PoemReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'poem_id', 'review', 'rating', 'reviewer']
    search_fields = ['review_id', 'poem_id', 'review', 'rating', 'reviewer'] 

class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content', 'cover', 'story_id']
    search_fields = ['title', 'story_id']

class StoryReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'story_id', 'review', 'rating', 'reviewer']
    search_fields = ['review_id', 'story_id', 'review', 'rating', 'reviewer']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content', 'cover', 'article_id']
    search_fields = ['title', 'article_id']

class ArticleReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'article_id', 'review', 'rating', 'reviewer']
    search_fields = ['review_id', 'article_id', 'review', 'rating', 'reviewer']

admin.site.register(Book, BookAdmin)
admin.site.register(BookReview, BookReviewAdmin)   
admin.site.register(Poem, PoemAdmin)
admin.site.register(PoemReview, PoemReviewAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryReview, StoryReviewAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleReview, ArticleReviewAdmin)   