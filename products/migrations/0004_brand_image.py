# Generated by Django 5.1.2 on 2024-10-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_subcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='brands/images/'),
        ),
    ]