# Generated by Django 4.1.7 on 2023-04-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0051_alter_db_web_notification_student_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_web_notification',
            name='academic_session',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]