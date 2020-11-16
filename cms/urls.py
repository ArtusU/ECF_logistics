from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.admin, name="admin"),

    path('monday-delivery/', views.mondayDelivery, name="monday-delivery"),

    path('run/', views.run, name="run"),
    path('order-details/<str:pk>', views.orderDetails, name="order-details"),
    path('referrer-dashboard/<str:pk>', views.referrerDashboard, name="referrer"),
]