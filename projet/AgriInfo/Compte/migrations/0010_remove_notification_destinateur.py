# Generated by Django 5.0.3 on 2024-05-05 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compte', '0009_utilisateur_notif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='destinateur',
        ),
    ]
