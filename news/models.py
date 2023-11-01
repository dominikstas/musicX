from django.db import models

class preordery(models.Model):
    TYPI_NOSNIKA = (
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
    )

    tytul = models.CharField(max_length=100)
    artysta = models.CharField(max_length=100)
    nosnik = models.CharField(max_length=10, choices=TYPI_NOSNIKA)
    data = models.IntegerField()
    zdjecie = models.CharField(max_length=1000)

    def __str__(self):
        return self.tytul