# Generated by Django 2.1.5 on 2019-07-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0010_auto_20190730_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='place_on_page',
            field=models.IntegerField(choices=[(0, 'Not ussed'), (1, 'First'), (2, 'Second'), (3, 'Third')], default=0),
        ),
    ]
