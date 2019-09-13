
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_view, name='index'),
    path('shop/product/<str:product_slug>/', views.product_view, name='product_detail'),
    path('shop/', views.newshop, name='newshop'),
    path('services/', views.services, name='services'),




]
