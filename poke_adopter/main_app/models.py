from django.db import models

# Create your models here.
class Pokemon(models.Model):
    img = models.CharField()
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()

    def __str__(self):
        return self.name