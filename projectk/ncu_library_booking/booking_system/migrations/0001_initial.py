# Generated by Django 5.2 on 2025-05-06 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KStudyArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='區域名稱')),
            ],
            options={
                'verbose_name': 'K書中心區域',
                'verbose_name_plural': 'K書中心區域',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=20, verbose_name='座位編號')),
                ('description', models.TextField(blank=True, null=True, verbose_name='座位描述')),
                ('is_available_for_booking', models.BooleanField(default=True, verbose_name='是否開放預約')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.kstudyarea', verbose_name='所屬區域')),
            ],
            options={
                'verbose_name': '座位',
                'verbose_name_plural': '座位',
                'unique_together': {('area', 'seat_number')},
            },
        ),
    ]
