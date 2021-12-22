# Generated by Django 3.2.9 on 2021-12-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_remove_products_prod_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prod_image',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='prod_price',
            field=models.CharField(default=1, max_length=250, verbose_name='price'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_decription',
            field=models.TextField(verbose_name='description'),
        ),
    ]
