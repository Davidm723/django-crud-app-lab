from django.contrib import admin
from .models import Pokemon, Battle, Item

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Battle)
admin.site.register(Item)