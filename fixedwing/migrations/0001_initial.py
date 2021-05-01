# Generated by Django 3.2 on 2021-04-21 05:16

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
            name='FixedWingPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateField()),
                ('Rotor_type', models.CharField(choices=[('BLDC', 'Electric motor'), ('IC', 'Internal combustion engine')], default='BLDC', max_length=4)),
                ('RF_frequecy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit', models.CharField(choices=[('MHz', 'Mega Hertz'), ('GHz', 'Giga Hertz')], default='GHz', max_length=3)),
                ('wingSpanInMm', models.IntegerField()),
                ('wingAreaInMm2', models.IntegerField()),
                ('averageChordInMm', models.IntegerField()),
                ('weightIn_grams', models.IntegerField()),
                ('cruiseSpeedInMPerS', models.IntegerField()),
                ('microcontroller', models.CharField(max_length=100)),
                ('inertialMeasurementUnit', models.CharField(max_length=100)),
                ('RCReceiver', models.CharField(max_length=250)),
                ('RCTransmitter', models.CharField(max_length=250)),
                ('servos', models.CharField(max_length=250)),
                ('electronicSpeedContorller', models.CharField(max_length=250)),
                ('brushlessMotor', models.CharField(max_length=250)),
                ('user_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FixedWingVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoFile', models.FileField(null=True, upload_to='videos')),
                ('videoInfo', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fixedwing.fixedwingpost')),
            ],
        ),
        migrations.CreateModel(
            name='FixedWingImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('imageInfo', models.CharField(default=None, max_length=300)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fixedwing.fixedwingpost')),
            ],
        ),
        migrations.CreateModel(
            name='FixedWingComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fixedwing_comments', to='fixedwing.fixedwingpost')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
