# Generated by Django 4.1.5 on 2023-04-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('bi', models.IntegerField(primary_key=True, serialize=False)),
                ('bn', models.CharField(max_length=100)),
                ('an', models.CharField(max_length=100)),
                ('sn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bookr',
            fields=[
                ('bi', models.IntegerField(primary_key=True, serialize=False)),
                ('bn', models.CharField(max_length=100)),
                ('an', models.CharField(max_length=100)),
                ('si', models.IntegerField()),
                ('se', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e', models.EmailField(max_length=254)),
                ('p', models.CharField(max_length=100)),
            ],
        ),
    ]
