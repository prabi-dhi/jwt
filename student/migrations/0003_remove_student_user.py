# Generated by Django 5.1.3 on 2024-12-05 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]