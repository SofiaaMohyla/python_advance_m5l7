from django.db import models

# Create your models here.
# models.py
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)  # Поле для збереження імені елемента

    def __str__(self):
        return self.name
