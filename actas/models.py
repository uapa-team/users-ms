from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Acta(models.Model):
    año = models.IntegerField(default=2020,validators=[
            MinValueValidator(1900),
            MaxValueValidator(2099)
        ])
    número = models.IntegerField(default=1,validators=[
            MinValueValidator(1),
            MaxValueValidator(52)
        ])

    def __str__(self):
        return str(self.año) + "-" + str(self.número)

    class Meta:
        unique_together = (("año", "número"),)
        db_table = "Acta"
        permissions = []