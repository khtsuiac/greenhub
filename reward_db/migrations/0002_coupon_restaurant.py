# Generated by Django 3.2.12 on 2022-04-13 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_db', '0003_auto_20220410_1857'),
        ('reward_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants_db.restaurant'),
        ),
    ]
