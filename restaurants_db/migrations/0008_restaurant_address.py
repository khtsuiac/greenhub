# Generated by Django 3.2.12 on 2022-04-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_db', '0007_alter_restaurant_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
