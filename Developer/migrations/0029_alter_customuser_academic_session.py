# Generated by Django 4.1.7 on 2023-04-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0028_alter_customuser_academic_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='academic_session',
            field=models.CharField(blank=True, choices=[('2022-23', '2022-23'), ('2023-24', '2023-24'), ('2024-25', '2024-25'), ('2025-26', '2025-26'), ('2026-27', '2026-27'), ('2028-28', '2028-28')], max_length=255, null=True),
        ),
    ]
