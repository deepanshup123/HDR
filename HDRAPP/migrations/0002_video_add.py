# Generated by Django 5.0.1 on 2024-02-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HDRAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='video/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
