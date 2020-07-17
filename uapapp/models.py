from django.db import models

TIPOS = [
    ("Pre", "Pregrado"),
    ("Pos", "Posgrado"),
]

class Dependencia(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("pre", "Puede descargar reportes de pregrado."),
            ("pos", "Puede descargar reportes de posgrado."),
        ]


class Programa(models.Model):
    nombre = models.CharField(max_length=60)
    dependencia = models.ForeignKey("Dependencia", on_delete=models.PROTECT)
    tipo = models.CharField(max_length=3, choices=TIPOS, default="PRE")

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("programa", "Puede descargar reportes del programa."),
        ]