from django.urls import path
from . import views

# Creating path to access page.
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
