# Generated by Django 3.2.4 on 2021-07-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portofolio', '0004_post_imagine_post1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagine_post2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='imagine_post3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
