from django.db import models
from django.db import models
from django.contrib.auth.models import User
    

TIPOS = [
    ("pre", "Pregrado"),
    ("pos", "Posgrado")
]

class Dependencia(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Dependencia"
        permissions = [
            ("pre", "Puede descargar reportes de pregrado."),
            ("pos", "Puede descargar reportes de posgrado.")
        ]


class Programa(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    dependencia = models.ForeignKey("Dependencia", on_delete=models.PROTECT)
    tipo = models.CharField(max_length=3, choices=TIPOS, default="pre")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Programa"
        permissions = [
            ("programa", "Puede descargar reportes.")
        ]

class UsuarioDependencia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)