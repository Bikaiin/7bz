from django.shortcuts import render
from ecomapp.models import Category, Product, Production
# Create your views here.


def index_view(request):

    Productions = Production.objects.all()
    products = Product.objects.all().filter(available=True)
    context = {

        'Productions': Productions,
        'products': products
    }

    return render(request, 'index.html', context)

def base_view(request):
    Productions = Production.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)
    context = {
        'Productions': Productions,
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    Productions = Production.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'Productions': Productions
    }
    return render(request, 'product.html', context)

def production_view(request, production_slug):
    Productions = Production.objects.all()
    product = Production.objects.get(slug=production_slug)
    context = {
        'product': product,
        'Productions': Productions
    }
    return render(request, 'production.html', context)



def category_view(request, category_slug):
    Productions = Production.objects.all()
    all_category= Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.all().filter(available=True, category=category)
    context = {
        'all_category':all_category,
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