# Generated by Django 4.1.7 on 2023-04-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0044_alter_db_fees_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='db_attendance',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
