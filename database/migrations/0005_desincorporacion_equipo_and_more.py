# Generated by Django 4.2.6 on 2023-11-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_rename_impresoras_impresora'),
    ]

    operations = [
        migrations.AddField(
            model_name='desincorporacion',
            name='equipo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='desincorporacion',
            name='descripcion',
            field=models.CharField(default='No asignado', max_length=100),
        ),
        migrations.AlterField(
            model_name='desincorporacion',
            name='marca',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='desincorporacion',
            name='modelo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ipv4',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='mac',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marca',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='modelo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='procesador',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='tipo_disco',
            field=models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='impresora',
            name='ipv4',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='impresora',
            name='mac',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='impresora',
            name='marca',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='impresora',
            name='modelo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='router',
            name='ipv4',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='router',
            name='mac',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='router',
            name='marca',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='router',
            name='modelo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='switch',
            name='ipv4',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='switch',
            name='mac',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='switch',
            name='marca',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='switch',
            name='modelo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='ipv4',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='mac',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='marca',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='modelo',
            field=models.CharField(default='No asignado', max_length=50),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='numero',
            field=models.CharField(default='No asignado', max_length=50),
        ),
    ]
