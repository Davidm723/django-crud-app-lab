from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import BattleForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, "pokemon/index.html", {"pokemon": pokemon})


def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    battle_form = BattleForm()
    return render(
        request, "pokemon/detail.html", {"pokemon": pokemon, "battle_form": battle_form}
    )


def add_battle(request, pokemon_id):
    form = BattleForm(request.POST)
    if form.is_valid():
        new_battle = form.save(commit=False)
        new_battle.pokemon_id = pokemon_id
        new_battle.save()
    return redirect("pokemon-detail", pokemon_id=pokemon_id)


class PokemonCreate(CreateView):
    model = Pokemon
    fields = "__all__"


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ["img", "description", "level"]


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = "/pokemon/"


class ItemCreate(CreateView):
    model = Item
    fields = "__all__"


class ItemList(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item


class ItemUpdate(UpdateView):
    model = Item
    fields = ["img", "description"]


class ItemDelete(DeleteView):
    model = Item
    success_url = "/items/"
