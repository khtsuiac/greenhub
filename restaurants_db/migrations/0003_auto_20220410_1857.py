# Generated by Django 3.2.12 on 2022-04-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_db', '0002_auto_20220410_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='district',
            field=models.CharField(choices=[('CW', 'Central and Western'), ('EA', 'Eastern'), ('IS', 'Islands'), ('KC', 'Kowloon City'), ('KI', 'Kwai Tsing'), ('KU', 'Kwun Tong'), ('NO', 'North'), ('SK', 'Sai Kung'), ('SS', 'Sham Shui Po'), ('ST', 'Sha Tin'), ('SO', 'Southern'), ('TP', 'Tai Po'), ('TW', 'Tsuen Wan'), ('TM', 'Tuen Mun'), ('WC', 'Wan Chai'), ('WT', 'Wong Tai Sin'), ('YT', 'Yau Tsim Mong'), ('YL', 'Yuen Long')], default='SK', max_length=2),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='region',
            field=models.CharField(choices=[('NT', 'New Territories'), ('KLN', 'Kowloon'), ('HK', 'Hong Kong Island')], default='NT', max_length=3),
        ),
    ]
