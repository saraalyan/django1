from django.urls import path,include
from . import views

urlpatterns = [
    path('author', views.index, name='index')
#hello
]
