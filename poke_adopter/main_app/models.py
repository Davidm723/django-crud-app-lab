from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TRAINERS = (("T", "Trainer"), ("R", "Rival"), ("G", "Gym Leader"))


# Create your models here.
class Item(models.Model):
    img = models.CharField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.id})


class Pokemon(models.Model):
    img = models.CharField()
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pokemon-detail", kwargs={"pokemon_id": self.id})


class Battle(models.Model):
    date = models.DateField("Battle Date")
    trainer = models.CharField(max_length=1, choices=TRAINERS, default=TRAINERS[0][0])

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_trainer_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
