from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('home/', views.home, name='home'),
    path('addItems/', views.addItems, name='addItems'),
    path('addToWishlist/', views.addToWishlist, name='addToWishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('userProfile/<str:pk>', views.userProfile, name='userProfile'),

    path('createAdmin/', views.createAdmin, name='createAdmin'),
    path('AdminHome/', views.adminHome, name='AdminHome'),

    path('AdminUsers/', views.adminUsers, name='AdminUsers'),
    path('AdminDelete/', views.adminDelete, name='AdminDelete'),
    path('AdminUpdate/', views.adminUpdate, name='AdminUpdate'),

    path('AdminItems/', views.adminItems, name='AdminItems'),
    path('AdminItemDelete/', views.adminDeleteItems, name='AdminItemDelete'),
    path('AdminItemUpdate/', views.adminUpdateItems, name='AdminItemUpdate'),

    path('AdminWishlist/', views.adminWishlist, name='AdminWishlist'),
    path('AdminWishDelete/', views.adminDeleteWish, name='AdminWishDelete'),
    path('AdminWishUpdate/', views.adminUpdateWish, name='AdminWishUpdate'),
]