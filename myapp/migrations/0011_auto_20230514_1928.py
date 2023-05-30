# Generated by Django 3.2.17 on 2023-05-14 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_departement_numagendadept'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaDept',
            fields=[
                ('numAgendaDept', models.IntegerField(primary_key=True, serialize=False)),
                ('dateMAJ', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='departement',
            name='numAgenda',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='numEmploye',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.employe'),
        ),
        migrations.AddField(
            model_name='departement',
            name='numAgendaDept',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='myapp.agendadept'),
            preserve_default=False,
        ),
    ]
