# Generated by Django 3.2.4 on 2021-07-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portofolio', '0006_post_git_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='git_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
