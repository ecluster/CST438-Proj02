from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    #path('login/', views.loginPage, name='login'),
    path('login2/', views.loginPage2, name='login2'),
    path('logout2', views.logoutPage, name='logout2'),
    #path('logout/', views.logoutUser, name='logout'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('home/', views.home, name='home'),
    path('addItems/', views.addItems, name='addItems'),
    path('addToWishlist/', views.addToWishlist, name='addToWishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('userProfile/<str:pk>', views.userProfile, name='userProfile'),

    path('AdminHome/', views.adminHome, name='AdminHome'),
    path('AdminUsers/', views.adminUsers, name='AdminUsers'),
    path('AdminDelete/', views.adminDelete, name='AdminDelete'),
    path('AdminUpdate/', views.adminUpdate, name='AdminUpdate'),
]