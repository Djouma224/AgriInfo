# Generated by Django 5.0.3 on 2024-04-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compte', '0002_utilisateur_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]