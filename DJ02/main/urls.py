from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('basics/', views.basics, name='basics'),
    path('equipment/', views.equipment, name='equipment'),
    path('tips/', views.tips, name='tips'),
    path('safety/', views.safety, name='safety'),
    path('news/', views.news, name='news'),
]
