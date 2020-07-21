from django.test import TestCase
from django_seed import Seed
from uapapp.models import Dependencia, Programa

class Seeding(TestCase):

    dependencias = ["Área curricular de ingniería civil y agrícola",
                    "Área curricular de ingniería química y ambiental", 
                    "Área curricular de ingniería mecánica y mecatrónica", 
                    "Área curricular de ingniería eléctrica y electrónica",
                    "Área curricular de ingniería sistemas e industrial",
                    ]

    seeder = Seed.seeder()

    for entry in dependencias:
        print(entry)
        seeder.add_entity(Dependencia, 1, {
            'nombre': entry
        })

    seeder.execute()
