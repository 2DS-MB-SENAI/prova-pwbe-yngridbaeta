# Generated by Django 4.2 on 2025-04-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(choices=[('Cirurgiao', 'Cirurgiao'), ('Oftalmologista', 'Oftalmologista'), ('Enfermeiro', 'Enfermeiro'), ('CAR', 'Cadiologista')], max_length=30),
        ),
    ]
