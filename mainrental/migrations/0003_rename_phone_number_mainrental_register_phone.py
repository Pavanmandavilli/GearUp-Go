# Generated by Django 5.0.2 on 2024-02-18 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainrental', '0002_mainrental_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainrental_register',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
