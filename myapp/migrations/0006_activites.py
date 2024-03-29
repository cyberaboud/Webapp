# Generated by Django 3.2.17 on 2023-05-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_absent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('numActivite', models.IntegerField(primary_key=True, serialize=False)),
                ('typeA', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1024)),
                ('dateAct', models.DateField()),
                ('hDebut', models.TimeField(blank=True, null=True)),
                ('hFin', models.TimeField(blank=True, null=True)),
                ('dateCreation', models.DateField()),
                ('createur', models.CharField(max_length=20)),
                ('visible', models.IntegerField()),
                ('numAgenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.agenda')),
            ],
        ),
    ]
