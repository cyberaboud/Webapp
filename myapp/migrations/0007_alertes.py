# Generated by Django 3.2.17 on 2023-05-14 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_activites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alertes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
                ('delais', models.DateField()),
                ('numActivite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.activites')),
            ],
        ),
    ]
