from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]
