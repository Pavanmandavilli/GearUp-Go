# Generated by Django 5.0.2 on 2024-02-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainrental_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
