# Generated by Django 5.0 on 2024-01-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ti', '0002_alter_image_ai_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='ai_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
