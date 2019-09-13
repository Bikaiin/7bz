from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse
from django import forms
from PIL import Image
import os
import logging
logging.basicConfig(filename="sample.log", level=logging.INFO)
# Create your models here.
PLACE_ON_PAGE = [(0, 'Not ussed'),
                 (1, 'First'),
                 (2, 'Second'),
                 (3, 'Third')]


def image_folder(instance, filename):
    if hasattr(instance, 'slug'):
        filename = instance.slug + '.' + filename.split('.')[1]
        return "{0}/{1}".format(instance.slug, filename)
    else:
        filename = instance.product.slug + '.' + filename.split('.')[1]
        return "{0}/{1}".format(instance.product.slug, filename)

def image_thumb_folder(instance, filename):
    original_image_path = str(instance.img).rsplit('/', 1)[0]
    return os.path.join(original_image_path, filename).replace("\\","/")


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to=image_folder, null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=300, blank=True, null=True)
    place_on_page = models.IntegerField(choices=PLACE_ON_PAGE,default=0)
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        url = "/shop/" + self.slug
        return url



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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    img = models.ImageField(upload_to=image_folder)
    image_thumb = models.CharField(('Thumbnail image'), max_length=255, blank=True)
    def __str__(self):
        return '%s ' % (self.product.title)
    def get_absolute_url(self):
        return reverse('ProductIMG_detail', kwargs={'ProductIMG_slug': self.product.slug})

    def get_thumb_image_url(self):

        return   "/media/" +self.image_thumb



    def save(self, *args, **kwargs):
            size = {'height': 256, 'width': 256}
            super(ProductIMG, self).save(*args, **kwargs)
            extension = str(self.img.url).rsplit('.', 1)[1]  # получаем расширение загруженного файла
            filename = str(self.img.url).rsplit('/', 1)[1].rsplit('.', 1)[0]  # получаем имя загруженного файла (без пути к нему и расширения)
            fullpath = str(self.img.path).rsplit(os.sep, 1)[0]  # получаем путь к файлу (без имени и расширения)




            if extension in ['jpg', 'jpeg', 'png', 'JPG']:    # если расширение входит в разрешенный список
                im = Image.open(str(self.img.path))  # открываем изображение
                im.thumbnail((size['width'], size['height'])) # создаем миниатюру указанной ширины и высоты (важно - im.thumbnail сохраняет пропорции изображения!)
                thumbname = filename + "_" + str(size['width']) + "x" + str(size['height']) + '.' + extension # имя нового изображения в формате oldname_60x60.jpg
                im.save(fullpath + '/' + thumbname) # сохраняем полученную миниатюру
                self.image_thumb = image_thumb_folder(self, thumbname) # записываем путь к ней в поле image_thumb в модели
                super(ProductIMG, self).save(*args, **kwargs)
