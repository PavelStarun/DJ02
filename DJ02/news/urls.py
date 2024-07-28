from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('news/', views.home, name='news_home'),
	path('news/<int:pk>/', views.news_detail, name='news_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)