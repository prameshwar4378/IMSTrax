# Generated by Django 4.2 on 2023-05-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0076_customuser_profile_valid_up_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_valid_up_to',
            field=models.DateField(null=True),
        ),
    ]