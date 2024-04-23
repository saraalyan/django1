from django.urls import path,include
from . import views

urlpatterns = [
    path('book', views.index, name='index')
]
