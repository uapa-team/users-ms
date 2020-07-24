from django.test import TestCase
from django_seed import Seed
from uapapp.models import Dependencia, Programa

#Seed each model with faker: python manage.py seed uapapp --number=20

class Seeding(TestCase):

    dependencias = ["Área curricular de ingeniería civil y agrícola",
                    "Área curricular de ingeniería química y ambiental", 
                    "Área curricular de ingeniería mecánica y mecatrónica", 
                    "Área curricular de ingeniería eléctrica y electrónica",
                    "Área curricular de ingeniería sistemas e industrial",
                    ]

    seeder = Seed.seeder()

    for entry in dependencias:
        seeder.add_entity(Dependencia, 1, {
            'nombre': entry
        })
        seeder.execute()
