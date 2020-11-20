from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.home, name="home"),

    #path('user/', views.userPage, name="user-page"),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('order-details/<str:pk>', views.orderDetails, name="order-details"),

    path('referrer/', views.referrerView, name="referrer-page"),
    path('referrer-settings/', views.referrerSettings, name="account-settings"),


    path('driver/', views.driverView, name="driver-page"),

    path('create-order/', views.createOrder, name="create-order"),
    path('update-order/<str:pk>', views.updateOrder, name="update-order"),
    path('delete-order/<str:pk>', views.deleteOrder, name="delete-order"),

]