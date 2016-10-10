from django.db import models


class Map(models.Model):
    title           =   models.CharField(max_length=500)
    question        =   models.TextField()
    description     =   models.TextField()
