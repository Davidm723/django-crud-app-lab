from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import BattleForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


@login_required
def pokemon_index(request):
    pokemon = Pokemon.objects.filter(user=request.user)
    return render(request, "pokemon/index.html", {"pokemon": pokemon})


@login_required
def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    items_pokemon_doesnt_have = Item.objects.exclude(
        id__in=pokemon.items.all().values_list("id")
    )
    battle_form = BattleForm()
    return render(
        request,
        "pokemon/detail.html",
        {
            "pokemon": pokemon,
            "battle_form": battle_form,
            "items": items_pokemon_doesnt_have,
        },
    )


@login_required
def add_battle(request, pokemon_id):
    form = BattleForm(request.POST)
    if form.is_valid():
        new_battle = form.save(commit=False)
        new_battle.pokemon_id = pokemon_id
        new_battle.save()
    return redirect("pokemon-detail", pokemon_id=pokemon_id)


@login_required
def associate_item(request, pokemon_id, item_id):
    Pokemon.objects.get(id=pokemon_id).items.add(item_id)
    return redirect("pokemon-detail", pokemon_id=pokemon_id)


@login_required
def remove_item(request, pokemon_id, item_id):
    Pokemon.objects.get(id=pokemon_id).items.remove(item_id)
    return redirect("pokemon-detail", pokemon_id=pokemon_id)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("pokemon-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ["img", "name", "types", "description", "level"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ["img", "description", "level"]


class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = "/pokemon/"


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = "__all__"


class ItemList(LoginRequiredMixin, ListView):
    model = Item


class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ["img", "description"]


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = "/items/"
