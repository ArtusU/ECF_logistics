from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.home, name="home"),
    
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
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="cms/password_reset.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='cms/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="cms/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="cms/password_reset_complete.html"), name="password_reset_complete"),

]