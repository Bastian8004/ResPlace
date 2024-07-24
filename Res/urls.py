from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_lane, name='book_lane'),
path('confirm/<int:reservation_id>/', views.reservation_confirm, name='reservation_confirm'),  # New URL pattern
]
