# Generated by Django 3.2.4 on 2021-07-08 18:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_product', '0002_alter_product_seller'),
        ('app_bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('user', 'product')},
        ),
    ]
