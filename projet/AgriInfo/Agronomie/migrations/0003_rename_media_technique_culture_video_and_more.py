# Generated by Django 5.0.3 on 2024-03-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agronomie', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technique_culture',
            old_name='media',
            new_name='video',
        ),
        migrations.AddField(
            model_name='technique_culture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='technque'),
        ),
    ]
