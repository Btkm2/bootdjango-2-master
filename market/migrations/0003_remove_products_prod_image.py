# Generated by Django 3.2.9 on 2021-11-30 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_products_prod_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='prod_image',
        ),
    ]