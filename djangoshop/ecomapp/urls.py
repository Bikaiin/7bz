
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_view, name='index'),
    path('shop/product/<str:product_slug>/', views.product_view, name='product_detail'),
    path('Production/<str:production_slug>/', views.production_view, name='production'),
    path('contacts', views.contacts_view, name='contacts'),
    path('uslugi/', views.uslugi_view, name='uslugi_view'),
    path('shop/', views.newshop, name='newshop'),
    path('services/', views.services, name='services'),




]
