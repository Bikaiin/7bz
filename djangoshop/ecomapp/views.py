from django.shortcuts import render
from ecomapp.models import Category, Product, Production, ProductIMG
import logging
# Create your views here.
logging.basicConfig(filename="sample.log", level=logging.INFO)

def index_view(request):
    place_on_page_1_filter = Category.objects.get(place_on_page = "1")
    place_on_page_2_filter = Category.objects.get(place_on_page = "2")
    Productions = Production.objects.all()
    products = Product.objects.all().filter()
    place_on_page_1 = Category.objects.all().filter(parent=place_on_page_1_filter)
    place_on_page_2 = Category.objects.all().filter(parent=place_on_page_2_filter)

    context = {

        'Productions': Productions,
        'products': products,
        'place_on_page_1': place_on_page_1,
        'place_on_page_2': place_on_page_2
    }

    return render(request, 'index.html', context)

def base_view(request):
    Productions = Production.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all().filter()
    for product in products:
        e = ProductIMG.objects.get(product=product)
        product.image = e.img
    context = {
        'Productions': Productions,
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    Productions = Production.objects.all()
    product = Product.objects.get(slug=product_slug)

    Imgs = ProductIMG.objects.filter(product=product)
    context = {
        'product': product,
        'Productions': Productions,
        'Images': Imgs
    }
    return render(request, 'product.html', context)

def production_view(request, production_slug):
    Productions = Production.objects.all()
    product = Production.objects.get(slug=production_slug)
    logging.info(product.image)
    context = {
        'product': product,
        'Productions': Productions,

    }
    return render(request, 'production.html', context)



def category_view(request, category_slug):
    Productions = Production.objects.all()
    all_category = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.all().filter(category=category)
    for product in products_of_category:
        e = ProductIMG.objects.get(product=product)
        product.image = e.img
    context = {
        'all_category': all_category,
        'category': category,
        'products_of_category': products_of_category,
        'Productions': Productions
    }
    return render(request, 'category.html', context)

def contacts_view(request):
    Productions = Production.objects.all()
    context = {

        'Productions': Productions
    }
    return render(request, 'contacts.html', context)