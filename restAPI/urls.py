from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('home/', views.home, name='home'),
    path('addItems/', views.addItems, name='addItems'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('user-detail/<str:uName>/', views.user_detail, name='user-detail'),
    path('user-items/<str:uId>/', views.items_list, name='user-items'),
]