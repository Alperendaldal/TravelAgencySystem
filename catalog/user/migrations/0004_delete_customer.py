# Generated by Django 5.0.6 on 2024-05-25 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0005_alter_reservation_reservation_customer_and_more'),
        ('user', '0003_user_remove_customer_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]