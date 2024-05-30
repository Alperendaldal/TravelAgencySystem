# Generated by Django 5.0.6 on 2024-05-25 11:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0006_alter_reservation_reservation_customer_and_more'),
        ('user', '0004_delete_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tel_No', models.CharField(max_length=10, null=True, verbose_name='Phone Number')),
                ('Emergency_Number', models.CharField(max_length=10, null=True)),
                ('Birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('Gender', models.CharField(max_length=10, null=True, verbose_name='Gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
