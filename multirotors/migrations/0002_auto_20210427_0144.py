# Generated by Django 3.2 on 2021-04-27 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multirotors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrotorscomment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mrotorsimages',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mrotorspost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mrotorsvideo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
