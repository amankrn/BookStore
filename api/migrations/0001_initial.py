# Generated by Django 5.0 on 2023-12-12 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
    ]