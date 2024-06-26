# Generated by Django 5.0.6 on 2024-05-22 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tour', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Reservation_Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customer'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Reservation_Employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tour.employee'),
        ),
        migrations.AddField(
            model_name='payment',
            name='Payment_ReservationID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tour.reservation'),
        ),
        migrations.AddField(
            model_name='tour',
            name='Trip_Employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tour.employee'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Reservation_Trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tour.tour'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='Travel_History_Reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tour.reservation'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='Travel_History_Trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tour.tour'),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='Travel_History_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customer'),
        ),
    ]
