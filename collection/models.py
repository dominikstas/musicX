from django.db import models


class Plyta(models.Model):
    id = models.IntegerField
    tytul = models.CharField(max_length=255)
    wykonawca = models.CharField(max_length=255)
    nosnik = models.CharField(max_length=50)
    # Dodaj inne pola modelu

    def __str__(self):
        return self.tytul
