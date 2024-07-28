from django.shortcuts import render
from .models import News_post

def news_detail(request, pk):
	new = News_post.objects.get(id=pk)
	return render(request, 'news/news_detail.html', {'new': new})

def home(request):
	news = News_post.objects.all()
	return render(request, 'news/news.html', {'news': news})

