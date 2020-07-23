# Generated by Django 3.0.8 on 2020-07-23 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'db_table': 'Dependencia',
                'permissions': [('pre', 'Puede descargar reportes de pregrado.'), ('pos', 'Puede descargar reportes de posgrado.')],
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('tipo', models.CharField(choices=[('pre', 'Pregrado'), ('pos', 'Posgrado')], default='pre', max_length=3)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uapapp.Dependencia')),
            ],
            options={
                'db_table': 'Programa',
                'permissions': [('programa', 'Puede descargar reportes.')],
            },
        ),
    ]
