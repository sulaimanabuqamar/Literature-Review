from django.urls import path
from .views import home, books, book_detail, user_login, stories, story_detail, articles, article_detail, poems, poem_detail
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('books/', books, name="books"),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('stories/', stories, name='stories'),
    path('story/<int:story_id>/', story_detail, name='story_details'),
    path('articles/', articles, name='articles'),
    path('article/<int:article_id>/', article_detail, name='article_details'),
    path('poems/', poems, name='poems'),
    path('poem/<int:poem_id>/', poem_detail, name='poem_details'), 
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
