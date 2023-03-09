from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

from .models import User


class Consejos(models.Model):
    CONSEJO_CHOICES = [
        ('Local', 'Consejo Local'),
        ('Curul', 'Curul Especial'),
    ]
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150, blank=True)
    logo = ImageField(upload_to="consejos/logos")
    description = models.TextField(max_length=500, blank=True)
    type_consejo = models.CharField(max_length=5, choices= CONSEJO_CHOICES)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

    def __str__(self):
        return self.name

