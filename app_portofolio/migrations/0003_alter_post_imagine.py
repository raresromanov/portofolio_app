# Generated by Django 3.2.4 on 2021-06-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portofolio', '0002_post_imagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagine',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
