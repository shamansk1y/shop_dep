# Generated by Django 4.1.7 on 2023-03-25 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_coupon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'ordering': ['-end_date'], 'verbose_name_plural': 'Купони на знижку'},
        ),
    ]
