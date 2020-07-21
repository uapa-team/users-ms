from django.db import models

TIPOS = [
    ("pre", "Pregrado"),
    ("pos", "Posgrado")
]

class Dependencia(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Dependencia"
        permissions = [
            ("pre", "Puede descargar reportes de pregrado."),
            ("pos", "Puede descargar reportes de posgrado.")
        ]


class Programa(models.Model):
    nombre = models.CharField(max_length=60)
    dependencia = models.ForeignKey("Dependencia", on_delete=models.PROTECT)
    tipo = models.CharField(max_length=3, choices=TIPOS, default="pre")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Programa"
        permissions = [
            ("programa", "Puede descargar reportes.")
        ]