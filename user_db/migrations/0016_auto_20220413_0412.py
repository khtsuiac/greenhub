# Generated by Django 3.2.12 on 2022-04-12 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_db', '0015_rename_location_id_record_restaurant_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='balance_value',
            new_name='balance_delta',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='g_cash_value',
            new_name='g_cash_delta',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
        migrations.RemoveField(
            model_name='record',
            name='status',
        ),
    ]