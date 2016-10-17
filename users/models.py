from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.PROTECT)
    image   = models.ImageField(upload_to='static/profiles', max_length=254)

    def __str__(self):
        return self.user.username
