# Generated by Django 3.2.12 on 2022-04-13 15:35

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_db', '0003_auto_20220410_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
