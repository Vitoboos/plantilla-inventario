# Generated by Django 4.2.6 on 2023-11-18 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perifericos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('equipo', models.CharField(choices=[('Monitor', 'Monitor'), ('Mouse', 'Mouse'), ('Teclado', 'Teclado')], default='No asignado', max_length=50)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
    ]
