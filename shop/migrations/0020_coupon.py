# Generated by Django 4.1.7 on 2023-03-25 00:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_subproductimage_slug_alter_subproductimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('uses_remaining', models.PositiveIntegerField(default=1)),
                ('status', models.BooleanField(default=False)),
                ('exclude_categories', models.ManyToManyField(blank=True, related_name='excluded_coupons', to='shop.category')),
                ('exclude_manufacturers', models.ManyToManyField(blank=True, related_name='excluded_coupons', to='shop.manufacturer')),
                ('products', models.ManyToManyField(blank=True, to='shop.product')),
            ],
        ),
    ]
