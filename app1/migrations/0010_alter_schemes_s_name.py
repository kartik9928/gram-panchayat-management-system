# Generated by Django 4.1.2 on 2023-10-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_complaint_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemes',
            name='s_name',
            field=models.CharField(max_length=50),
        ),
    ]
