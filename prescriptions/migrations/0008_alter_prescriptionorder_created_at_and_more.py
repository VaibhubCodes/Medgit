# Generated by Django 5.1.2 on 2024-10-22 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0007_prescriptionorder_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptionorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='prescriptionorder',
            name='prescription',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='prescriptions.prescription'),
        ),
        migrations.AlterField(
            model_name='prescriptionorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]