# Generated by Django 2.1.5 on 2019-07-30 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_category_description1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description1',
        ),
    ]