# Generated by Django 4.1.7 on 2023-04-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0024_alter_customuser_student_prn_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_fees',
            name='academic_session',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_result',
            name='academic_session',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_schedule_exam',
            name='academic_session',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
