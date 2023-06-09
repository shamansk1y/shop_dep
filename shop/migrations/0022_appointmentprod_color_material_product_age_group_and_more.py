# Generated by Django 4.1.7 on 2023-03-28 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_coupon_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Призначення товару',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Варіанти кольорів',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Матеріал товару',
                'ordering': ('position',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='age_group',
            field=models.CharField(blank=True, choices=[('Д', 'Дорослий'), ('К', 'Дитячий'), ('Т', 'Підлітковий'), ('А', 'Дорослий, Дитячий')], max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='characteristics_gender',
            field=models.CharField(blank=True, choices=[('Ч', 'Чоловічий'), ('Ж', 'Жіночий'), ('У', 'Унісекс')], max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='appointment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.appointmentprod'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.material'),
        ),
    ]
