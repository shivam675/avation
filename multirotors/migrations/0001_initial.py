# Generated by Django 3.0.3 on 2021-04-25 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mRotorsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateField()),
                ('Rotor_type', models.CharField(choices=[('BLDC', 'BDC')], default='BLDC', max_length=4)),
                ('RF_frequecy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit', models.CharField(choices=[('MHz', 'Mega Hertz'), ('GHz', 'Giga Hertz')], default='GHz', max_length=3)),
                ('user_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mRotorsVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(null=True, upload_to='vedios')),
                ('video_info', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='multirotors.mRotorsPost')),
            ],
        ),
        migrations.CreateModel(
            name='mRotorsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('image_info', models.CharField(default=None, max_length=300)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='multirotors.mRotorsPost')),
            ],
        ),
        migrations.CreateModel(
            name='mRotorsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mRotors_comments', to='multirotors.mRotorsPost')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
