# Generated by Django 5.0 on 2024-01-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='ai_image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
