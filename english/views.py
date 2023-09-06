from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookReview, Poem, PoemReview, Story, StoryReview, Article, ArticleReview
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home.html")

def books(request):
    all_books = Book.objects.all()
    context = {
        'book_list': all_books
    }
    return render(request, "books.html", context)

@login_required
def book_detail(request, book_id):
 
    book_detail = get_object_or_404(Book, pk=book_id)
    book_reviews = BookReview.objects.all()
    
    if request.method == 'POST':
        review_text = request.POST['review']
        rating = int(request.POST['rating'])
        
        reviewer = request.user if request.user.is_authenticated else None
        review = BookReview(book_id=book_detail, review=review_text, rating=rating, reviewer=reviewer)
        review.save()
        
        return redirect('book_detail', book_id=book_id)
    
    context = {
        'book_detail': book_detail,
        'book_reviews': book_reviews,
    }
    return render(request, 'book_details.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'login.html')

def poems(request):
    all_poems = Poem.objects.all()
    context = {
        'poem_list': all_poems
    }
    return render(request, "poems.html", context)

@login_required
def poem_detail(request, poem_id):
 
    poem_detail = get_object_or_404(Poem, pk=poem_id)
    poem_reviews = PoemReview.objects.filter(poem_id=poem_id)
    
    if request.method == 'POST':
        review_text = request.POST['review']
        rating = int(request.POST['rating'])
        
        reviewer = request.user if request.user.is_authenticated else None
        review = PoemReview(poem_id=poem_detail, review=review_text, rating=rating, reviewer=reviewer)
        review.save()
        
        return redirect('poem_details', poem_id=poem_id)
    
    context = {
        'poem_detail': poem_detail,
        'poem_reviews': poem_reviews,
    }
    return render(request, 'poem_details.html', context)

def stories(request):
    all_stories = Story.objects.all()
    context = {
        'story_list': all_stories
    }
    return render(request, "stories.html", context)

@login_required
def story_detail(request, story_id):
 
    story_detail = get_object_or_404(Story, pk=story_id)
    story_reviews = StoryReview.objects.filter(story_id=story_id)
    
    if request.method == 'POST':
        review_text = request.POST['review']
        rating = int(request.POST['rating'])
        
        reviewer = request.user if request.user.is_authenticated else None
        review = StoryReview(story_id=story_detail, review=review_text, rating=rating, reviewer=reviewer)
        review.save()
        
        return redirect('story_detail', story_id=story_id)
    
    context = {
        'story_detail': story_detail,
        'story_reviews': story_reviews,
    }
    return render(request, 'story_details.html', context)


def articles(request):
    all_articles = Article.objects.all()
    context = {
        'article_list': all_articles
    }
    return render(request, "articles.html", context)

@login_required
def article_detail(request, article_id):
 
    article_detail = get_object_or_404(Article, pk=article_id)
    article_reviews = ArticleReview.objects.filter(article_id=article_id)
    
    if request.method == 'POST':
        review_text = request.POST['review']
        rating = int(request.POST['rating'])
        
        reviewer = request.user if request.user.is_authenticated else None
        review = ArticleReview(article_id=article_detail, review=review_text, rating=rating, reviewer=reviewer)
        review.save()
        
        return redirect('article_details', article_id=article_id)
    
    context = {
        'article_detail': article_detail,
        'article_reviews': article_reviews,
    }
    return render(request, 'article_details.html', context)