from django.db import models

class Plyta(models.Model):
    TYPI_NOSNIKA = (
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
    )

    tytul = models.CharField(max_length=100)
    artysta = models.CharField(max_length=100)
    nosnik = models.CharField(max_length=10, choices=TYPI_NOSNIKA)
    rok_zakupu = models.IntegerField()
    zdjecie = models.CharField(max_length=1000)

    # inne pola modelu

    def __str__(self):
        return self.tytul
