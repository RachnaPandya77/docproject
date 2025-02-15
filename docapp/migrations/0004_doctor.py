# Generated by Django 4.1 on 2025-02-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
