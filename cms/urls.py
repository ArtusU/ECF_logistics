from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('order-details/<str:pk>', views.orderDetails, name="order-details"),

    path('referrer-dashboard/<str:pk>', views.referrerDashboard, name="referrer"),

    path('create-order/', views.createOrder, name="create-order"),
    path('update-order/<str:pk>', views.updateOrder, name="update-order"),
    path('delete-order/<str:pk>', views.deleteOrder, name="delete-order"),

]