# Generated by Django 5.0.7 on 2024-08-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0002_remove_wanguser_emmail_wanguser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanguser',
            name='email',
            field=models.EmailField(max_length=32),
        ),
        migrations.AlterField(
            model_name='wanguser',
            name='password',
            field=models.IntegerField(max_length=12),
        ),
    ]