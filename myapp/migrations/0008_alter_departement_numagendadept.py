# Generated by Django 3.2.17 on 2023-05-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alertes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='numAgendaDept',
            field=models.IntegerField(default=0, null=True),
        ),
    ]