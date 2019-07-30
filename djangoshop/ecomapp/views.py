from django.shortcuts import render
from ecomapp.models import Category, Product, Production, ProductIMG
import logging
# Create your views here.
logging.basicConfig(filename="sample.log", level=logging.INFO)

def index_view(request):
    promo_category = Category.objects.get(name = "Рекламная продукция")
    packaging = Category.objects.get(name = "коробки")
    Productions = Production.objects.all()
    products = Product.objects.all().filter()
    packagings = Category.objects.all().filter(parent=packaging)
    promos = Category.objects.all().filter(parent=promo_category)
    logging.info(packagings[1].description)
    logging.info(promos[1].description)
    context = {

        'Productions': Productions,
        'products': products,
        'promos': promos,
        'packagings': packagings
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