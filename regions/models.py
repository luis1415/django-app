from django.db import models


class Commune(models.Model):
    states = [('A', 'Activo'), ('I', 'Inactivo'),]
    id_commune = models.CharField(max_length=100, unique=True)
    commune_name = models.CharField(max_length=100)
    state = models.CharField(max_length=1, choices=states, default='Activo')

    def __str__(self):
        return self.commune_name


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    commune = models.ManyToManyField(Commune)
    region_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.region_name
    