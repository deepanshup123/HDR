# Generated by Django 5.0.1 on 2024-03-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HDRAPP', '0011_remembers_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('otp', models.IntegerField()),
            ],
        ),
    ]
