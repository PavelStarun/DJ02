from django.shortcuts import render, get_object_or_404
from .models import News_post

def news(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_detail(request, pk):
    post = get_object_or_404(News_post, pk=pk)
    return render(request, 'news/news_detail.html', {'post': post})
