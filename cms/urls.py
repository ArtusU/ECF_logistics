from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.home),
    path('delivery-day/', views.delivery),
    path('run/', views.run),
    path('order-details/<str:pk>', views.orderDetails),
    path('referrer-dashboard/<str:pk>', views.referrerDashboard),
]