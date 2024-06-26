# Generated by Django 5.0.6 on 2024-05-22 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Total', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Total Price')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reservation_Time', models.DateTimeField(auto_now_add=True, verbose_name='Reservation Date')),
                ('Reservation_Price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Reservation Price')),
                ('Reservation_Note', models.TextField(verbose_name='Note')),
                ('Reservation_Confirmation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trip_Name', models.CharField(max_length=100, verbose_name='Trip Name')),
                ('Trip_Type', models.CharField(max_length=50, verbose_name='Trip Type')),
                ('Trip_Price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Price')),
                ('Trip_Capacity', models.IntegerField(verbose_name='Capacity')),
                ('Trip_Transportation', models.CharField(max_length=100, verbose_name='Transportation')),
                ('Trip_Accomadation', models.CharField(max_length=50, verbose_name='Accomadation')),
                ('Created_Date', models.DateTimeField(verbose_name='Trip Date')),
                ('Trip_image', models.CharField(max_length=50, verbose_name='Trip İmage')),
            ],
        ),
        migrations.CreateModel(
            name='TravelHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Travel_History_Created_Date', models.DateTimeField(verbose_name='Record Date')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=50, verbose_name='Employee Name')),
                ('Employee_Surname', models.CharField(max_length=50, verbose_name='Employee Surname')),
                ('Employee_Username', models.CharField(max_length=30, verbose_name='User Name')),
                ('Employee_Password', models.CharField(max_length=50, verbose_name='Password')),
                ('Employee_Job', models.CharField(max_length=50, verbose_name='Job Desciption')),
                ('Employee_SuperID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='Tour.employee')),
            ],
        ),
    ]
