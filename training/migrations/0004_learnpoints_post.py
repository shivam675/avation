# Generated by Django 3.2 on 2021-04-24 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_learnpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnpoints',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.training'),
        ),
    ]