from django.db import models
from django.contrib.auth.models import User

class Map(models.Model):
    user            =   models.ForeignKey(User, related_name='User', null=True)
    title           =   models.CharField(max_length=500)
    question        =   models.TextField()
    description     =   models.TextField()

    def __str__(self):
        return self.title
