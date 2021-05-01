# Generated by Django 3.2 on 2021-04-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0002_alter_userprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('message', models.TextField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
