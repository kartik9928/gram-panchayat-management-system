# Generated by Django 4.1.2 on 2023-01-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='schemes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField()),
                ('s_name', models.CharField(max_length=20)),
                ('s_detail', models.CharField(max_length=100)),
            ],
        ),
    ]