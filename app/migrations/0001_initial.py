# Generated by Django 4.0.4 on 2022-05-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('product_name', models.CharField(max_length=40)),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('title', models.CharField(max_length=40)),
                ('start', models.DateField()),
                ('state', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=40)),
                ('rank', models.IntegerField()),
                ('since', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]