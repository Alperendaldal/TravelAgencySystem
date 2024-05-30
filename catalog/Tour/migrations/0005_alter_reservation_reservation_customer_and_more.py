# Generated by Django 5.0.6 on 2024-05-25 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0004_alter_tour_trip_detail'),
        ('user', '0003_user_remove_customer_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Reservation_Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
        migrations.AlterField(
            model_name='travelhistory',
            name='Travel_History_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
    ]
