"""MainApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from restAPI import views

urlpatterns = [
    path('', include('restAPI.urls')),
    path('admin/', admin.site.urls),

    path('users/', views.users_list, name='users'),
    path('user-detail/<str:uName>/', views.user_detail, name='user-detail'),
    path('user-delete/<str:uName>/', views.deleteUser, name='user-delete'),
    path('user-update/<str:uName>/', views.updateUser, name='user-update'),

    path('user-change/<str:uId>/<str:uName>/<str:uPassword>/', views.update_user, name='user-change'),

    path('wishlist_user/<str:uId>/', views.wishlist_user, name='wishlist_user'),
    path('all-user-items/<str:uId>/', views.items_list, name='user-items'),
    path('specific-wishlitst-items/<str:wId>/', views.wishlist_item_list, name='specific-wishlitst-items'),
    path('wish-list-api/', views.wish_list_api, name='wish-list-api'),
    path('wish-delete/<str:wId>/', views.deleteWish, name='wish-delete'),
    path('wish-change/<str:wId>/<str:uId>/<str:iId>/', views.update_wish, name='wish-change'),
    path('wish-update/<str:wId>/', views.updateWish, name='wish-update'),

    path('item-list-API/', views.items_list_api, name='item-list-API'),
    path('item-delete/<str:iId>/', views.deleteItem, name='item-delete'),
    path('item-change/<str:iId>/<str:iName>/<str:iImgURl>/<str:iWebURL>/', views.update_item, name='item-change'),
    path('item-update/<str:iId>/', views.updateItem, name='item-update'),
    path('item-detail/<str:iId>/', views.item_detail, name='item-detail'),
    path('create-item/', views.create_item, name='create-item'),
    path('create-wishlist/', views.create_wishlist, name='create-wishlist'),

]
