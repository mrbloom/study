from django.urls import path

from . import views

urlpatterns = [
    path('part1/', views.index, name='index'),
]