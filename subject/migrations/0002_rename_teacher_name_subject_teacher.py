# Generated by Django 5.1.3 on 2024-12-06 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='teacher_name',
            new_name='teacher',
        ),
    ]
