# Generated by Django 5.0.6 on 2024-05-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='Trip_Detail',
            field=models.TextField(null=True, verbose_name='Tour descirption'),
        ),
    ]
