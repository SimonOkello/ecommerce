# Generated by Django 3.0.4 on 2020-03-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
