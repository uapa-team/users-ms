# Generated by Django 3.0.8 on 2020-07-23 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2099)])),
                ('número', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(52)])),
            ],
            options={
                'db_table': 'Acta',
                'permissions': [],
                'unique_together': {('año', 'número')},
            },
        ),
    ]
