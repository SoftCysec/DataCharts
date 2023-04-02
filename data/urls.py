from django.urls import path
from data import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results'),
]
