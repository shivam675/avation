# Generated by Django 3.2 on 2021-04-21 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixedwing', '0002_auto_20210421_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixedwingpost',
            name='user_name',
        ),
    ]
