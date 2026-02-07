from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


class Pokemon:
    def __init__(self, img, name, types, description, level):
        self.img = img
        self.name = name
        self.types = types
        self.description = description
        self.level = level


pokemons = [
    Pokemon(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "Pikachu",
        "Electric",
        "Mouse Pokemon",
        5,
    ),
    Pokemon(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/173.png",
        "Cleffa",
        "Fairy",
        "Star Shape Pokemon",
        2,
    ),
    Pokemon(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/174.png",
        "Igglybuff",
        "Normal, Fairy",
        "Balloon Pokemon",
        3,
    ),
]


def pokemon_index(request):
    return render(request, "pokemon/index.html", {"pokemons": pokemons})
