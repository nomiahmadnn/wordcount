
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count),
    path('about/', views.about, name='about'),
    path('residential/', views.residential, name='residential')
]
