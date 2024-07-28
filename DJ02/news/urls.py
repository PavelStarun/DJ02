from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
]
