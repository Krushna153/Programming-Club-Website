# Generated by Django 3.0.5 on 2020-06-17 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='date',
            new_name='date_time',
        ),
    ]
