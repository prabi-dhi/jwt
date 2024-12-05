# Generated by Django 5.1.3 on 2024-12-05 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
        ('student', '0006_remove_student_class_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_enrolled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom'),
        ),
    ]
