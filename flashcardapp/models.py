# w flashcardapp/models.py
from django.db import models

class NiemieckieSlowo(models.Model):
    slowo_niemieckie = models.CharField(max_length=100)
    slowo_polskie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.slowo_niemieckie} - {self.slowo_polskie}"
