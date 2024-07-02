from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_party, name='book_party'),
    path('party_list/', views.party_list, name='party_list'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]