# Generated by Django 4.1.2 on 2023-01-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_schemes'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_name', models.CharField(max_length=100)),
                ('n_date', models.DateField()),
                ('n_detail', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
