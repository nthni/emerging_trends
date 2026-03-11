from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about_highschool, name='about_highschool'),
        path('enroll/', views.enroll, name='enroll'),
    ]
