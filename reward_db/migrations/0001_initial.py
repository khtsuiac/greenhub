# Generated by Django 3.2.12 on 2022-04-12 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_db', '0005_auto_20220412_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('provider', models.CharField(max_length=100)),
                ('illustration', models.ImageField(upload_to='rewards')),
                ('cost', models.IntegerField(default=1000, verbose_name='G-cashed needed to redeem')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('reward_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reward_db.reward')),
                ('discount', models.IntegerField(default=3)),
                ('min_consume', models.IntegerField(default=20)),
            ],
            bases=('reward_db.reward',),
        ),
        migrations.CreateModel(
            name='Reward_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeem_id', models.UUIDField()),
                ('status', models.CharField(default='ACTIVE', max_length=5, verbose_name='ACTIVE, USED')),
                ('redeem_date', models.DateTimeField()),
                ('used_date', models.DateTimeField()),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reward_db.reward')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_db.user')),
            ],
        ),
    ]
