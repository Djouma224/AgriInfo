# Generated by Django 5.0.1 on 2024-03-05 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agronomie', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='actualite',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='culture',
            name='categorie_culture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agronomie.categorie_culture'),
        ),
        migrations.AddField(
            model_name='endroit_propice',
            name='culture',
            field=models.ManyToManyField(to='Agronomie.culture'),
        ),
        migrations.AddField(
            model_name='technique_culture',
            name='categorie_culture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agronomie.categorie_culture'),
        ),
    ]
