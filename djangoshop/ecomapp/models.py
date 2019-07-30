from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
#from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.
def image_folder(instance, filename):
    if hasattr(instance, 'slug'):
        filename = instance.slug + '.' + filename.split('.')[1]
        return "{0}/{1}".format(instance.slug, filename)
    else:
        filename = instance.product.slug + '.' + filename.split('.')[1]
        return "{0}/{1}".format(instance.product.slug, filename)




class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to=image_folder, null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=300, blank=True, null=True,)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

def pre_save_category_slug(sender, instance, *args, **kwargs):

    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug


def  pre_save_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.title, reversed=True))
        instance.slug = slug

def pre_save_img_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.product, reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)




'''
class ProductManager(models.Manager):
    def all(self, *arg, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)
'''
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

pre_save.connect(pre_save_product_slug, sender=Product)

class Production(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('production', kwargs={'production_slug': self.slug})

class ProductIMG(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    view = models.CharField(max_length=100)
    img = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return '%s %s' % (self.product.title, self.view)
    def get_absolute_url(self):
        return reverse('ProductIMG_detail', kwargs={'ProductIMG_slug': self.product.slug})





