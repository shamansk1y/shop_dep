# Generated by Django 4.1.7 on 2023-03-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0002_alter_infopage_options_alter_infopage_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='info_page/%Y/'),
        ),
    ]
