# Generated by Django 4.1.1 on 2022-10-08 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requiredfields',
            old_name='couraseduration',
            new_name='courseduration',
        ),
    ]