# Generated by Django 3.2.12 on 2022-04-11 19:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(choices=[('B', 'BORROW'), ('R', 'RETURE'), ('T', 'TOP UP')], max_length=1)),
                ('date_time', models.DateTimeField(verbose_name='date returned')),
                ('location_id', models.UUIDField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeem_date', models.DateTimeField()),
                ('reward_id', models.UUIDField()),
                ('status', models.DateTimeField(default='ACTIVE', max_length=20, verbose_name='ACTIVE, USED')),
                ('used_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('g_cash', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_db.record')),
                ('rewards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_db.reward')),
            ],
        ),
    ]
