# Generated by Django 5.0.7 on 2024-08-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_alter_banner_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
