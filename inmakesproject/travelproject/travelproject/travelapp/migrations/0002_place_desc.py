# Generated by Django 4.1.3 on 2022-11-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
