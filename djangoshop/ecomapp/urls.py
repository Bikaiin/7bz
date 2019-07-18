
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_view, name='index'),
    path('shop/', views.base_view, name='base'),
    path('shop/product/<str:product_slug>/', views.product_view, name='product_detail'),
    path('shop/category/<str:category_slug>/', views.category_view, name='category_detail'),
    path('Production/<str:production_slug>/', views.production_view, name='production'),
    path('contacts', views.contacts_view, name='contacts'),



]
