from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_party, name='book'),
]