from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_request, name='login'),
    path('signup/',views.signup, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
    path('verific/', views.verific, name='verific'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('cart_product/', views.cart_product, name='cart_product'),
    path('wishlist_product/', views.wishlist_product, name='wishlist_product'),
    path('cart_all_product/', views.cart_all_product, name='cart_all_product'),
    path('product_review/', views.product_review, name='product_review'),
]