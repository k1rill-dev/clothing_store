# Generated by Django 5.0 on 2023-12-20 11:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clothing_store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BagSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sell', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('basket', models.ManyToManyField(to='clothing_store.bag', verbose_name='Товары')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Продажа сумок',
                'verbose_name_plural': 'Продажи сумок',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FurCoatSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sell', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('basket', models.ManyToManyField(to='clothing_store.furcoat', verbose_name='Товары')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Продажа шуб',
                'verbose_name_plural': 'Продажи шуб',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GlovesSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sell', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('basket', models.ManyToManyField(to='clothing_store.gloves', verbose_name='Товары')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Продажа перчаток',
                'verbose_name_plural': 'Продажи перчаток',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HatSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sell', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('basket', models.ManyToManyField(to='clothing_store.hat', verbose_name='Товары')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Продажа шапок',
                'verbose_name_plural': 'Продажи шапок',
                'managed': True,
            },
        ),
    ]
