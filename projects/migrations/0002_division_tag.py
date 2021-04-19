# Generated by Django 3.2 on 2021-04-19 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('colour', models.CharField(choices=[('primary', 'ORANGE'), ('info', 'BLUE'), ('success', 'GREEN'), ('warning', 'YELLOW'), ('danger', 'RED'), ('neutral', 'GREY')], default='warning', max_length=12)),
                ('heading', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=300)),
                ('division', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='projects.division')),
            ],
        ),
    ]
