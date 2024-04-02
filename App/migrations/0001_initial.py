# Generated by Django 4.2.11 on 2024-04-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatrue', models.CharField(max_length=255)),
                ('humidity', models.CharField(max_length=255)),
                ('weather', models.CharField(max_length=255)),
                ('wind_speed', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('create_as', models.DateTimeField(auto_now_add=True)),
                ('update_as', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
