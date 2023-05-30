# Generated by Django 3.2.17 on 2023-05-14 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('numAgenda', models.IntegerField(primary_key=True, serialize=False)),
                ('dateCreation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=40)),
                ('numChef', models.IntegerField()),
                ('numAgendaDept', models.IntegerField()),
                ('numAgenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('numEmploye', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=20)),
                ('telIntern', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=40)),
                ('niveau', models.IntegerField()),
                ('numDept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.departement')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='numEmploye',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employe'),
        ),
    ]
