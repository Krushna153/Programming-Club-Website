# Generated by Django 3.0.5 on 2020-06-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20200617_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_description', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]