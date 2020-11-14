from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.home),
    path('delivery-day/', views.delivery),
    path('run/', views.run),
]