# Generated by Django 3.2 on 2021-04-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav', '0002_auto_20210417_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uavimages',
            name='images',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='uavpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
