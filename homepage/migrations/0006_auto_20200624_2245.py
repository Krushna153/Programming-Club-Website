# Generated by Django 3.0.5 on 2020-06-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_resources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcements',
            name='img',
        ),
        migrations.RemoveField(
            model_name='announcements',
            name='title_description',
        ),
        migrations.AlterField(
            model_name='announcements',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='events',
            name='title_description',
            field=models.CharField(max_length=1000),
        ),
    ]
