from django.shortcuts import render
from ecomapp.models import Category, Product, Production, ProductIMG
import logging
from django.http import JsonResponse

from django.core import serializers

# Create your views here.
logging.basicConfig(filename="sample.log", level=logging.INFO)

def index_view(request):
    place_on_page_1_filter = Category.objects.get(place_on_page = "1")
    logging.info(place_on_page_1_filter)
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
    categories = Category.objects.exclude(parent=None)
    products = Product.objects.all().filter()
    for product in products:
        Imgs = ProductIMG.objects.filter(product=product)
        product.image = '/media/' + Imgs[0].image_thumb
        logging.info(product.image)

    context = {
        'Productions': Productions,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop.html', context)


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
        e = ProductIMG.objects.filter(product=product)
        product.image = e[0].img
    context = {
        'all_category': all_category,
        'category': category,
        'products_of_category': products_of_category,
        'Productions': Productions
    }
    return render(request, 'category.html', context)

def category_json(request, category_slug):
    if category_slug == "all":
        products_of_category = Product.objects.all()
    else:
        category = Category.objects.get(slug=category_slug)
        products_of_category = Product.objects.all().filter(category=category)

    responce_data =[]

    for product in products_of_category:
        e = ProductIMG.objects.filter(product=product)
        pruduct_title = product.title
        product_description = product.description
        product_image_path = '/media/' + e[0].image_thumb.replace("\\","/")
        record = {"title":pruduct_title, "description":product_description,"image_path":product_image_path }
        responce_data.append(record)



    return JsonResponse({'data':responce_data})


def contacts_view(request):
    Productions = Production.objects.all()
    context = {

        'Productions': Productions
    }
    return render(request, 'contacts.html', context)

def category_view(request, category_slug):
    categories = Category.objects.exclude(parent=None)
    products = Product.objects.all().filter()
    for product in products:
        Imgs = ProductIMG.objects.filter(product=product)
        product.image = '/media/' + Imgs[0].image_thumb
        logging.info(product.image)

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', context)

def shop_view(request, category_slug):
    categories = Category.objects.exclude(parent=None)
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.all().filter(category=category)
    for product in products_of_category:
        Imgs = ProductIMG.objects.filter(product=product)
        product.image = '/media/' + Imgs[0].image_thumb
        logging.info(product.image)
    context = {
        'categories': categories,
        'products': products_of_category
    }

    return render(request, 'shop.html', context)
def uslugi_view(request):

    return render(request, 'uslugi.html')


def newshop(request):
    req_category = request.GET.get("category", "all")
    if req_category == "all":
        products_of_category = Product.objects.all()
    else:
        category = Category.objects.get(slug=req_category)
        products_of_category = Product.objects.all().filter(category=category)

    for product in products_of_category:
        img = ProductIMG.objects.filter(product=product)
        product.image = '/media/' + img[0].image_thumb.replace("\\", "/")

    if request.is_ajax():

        responce_data = []
        for product in products_of_category:

            pruduct_title = product.title
            product_description = product.description
            product_image_path = product.image
            record = {"title": pruduct_title, "description": product_description, "image_path": product_image_path}
            responce_data.append(record)

        return JsonResponse({'data': responce_data})
    else:
        categories = Category.objects.exclude(parent=None)

        context = {
            'categories': categories,
            'products': products_of_category,
        }
        return render(request, 'shop.html', context)
