# Generated by Django 4.1.5 on 2023-01-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_instituto_alter_estudiantes_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
