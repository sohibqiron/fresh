# Generated by Django 4.0.2 on 2022-02-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='employee')),
                ('salary', models.FloatField()),
            ],
        ),
    ]
