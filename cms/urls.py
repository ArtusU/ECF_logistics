from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('delivery-day/', views.delivery),
    path('run/', views.run),
]