# Generated by Django 5.0 on 2023-12-15 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_cart_user_orderitem_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_cart',
            field=models.BooleanField(default=False),
        ),
    ]
