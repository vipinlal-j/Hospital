# Generated by Django 5.1.4 on 2025-01-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_staffdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdb',
            name='DOB',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
