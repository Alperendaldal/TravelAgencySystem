# Generated by Django 5.0.6 on 2024-05-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='E_Posta',
            field=models.EmailField(max_length=50, null=True, verbose_name='Customer E-posta'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Emergency_Number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Gender',
            field=models.CharField(max_length=10, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Tel_No',
            field=models.CharField(max_length=10, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Customer Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='groups',
            field=models.ManyToManyField(null=True, related_name='customer_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Customer Lastname'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_permissions',
            field=models.ManyToManyField(null=True, related_name='customer_permissions', to='auth.permission'),
        ),
    ]
