# Generated by Django 2.1.5 on 2019-07-19 12:27

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=ecomapp.models.image_folder),
        ),
    ]
