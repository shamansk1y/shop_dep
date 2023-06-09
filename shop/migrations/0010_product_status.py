# Generated by Django 4.1.7 on 2023-03-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_characteristics_gender_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('Н', 'Немає в наявності'), ('В', 'В наявності'), ('П', 'Під замовлення 2-3 дні'), ('З', 'Під замовлення 2-4 тижні'), ('C', 'Скоро в наявності')], default='Н', max_length=1),
        ),
    ]
