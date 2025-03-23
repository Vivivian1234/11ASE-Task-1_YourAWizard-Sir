import requests # Must import requests so we can use API

# API Base URL for PokéAPI
API_URL = "https://pokeapi.co/api/v2/pokemon/"

# Dictionary to store collected Pokémon
pokedex = {}

def search_pokemon(name):
    """\nSearch for a Pokémon by name or ID and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }
        return pokemon_info 
    else:
        print("\nPokémon not found.")
        return None

def add_pokemon(name):
    """\nAdd a Pokémon to the Pokédex."""
    pokemon = search_pokemon(name)  
    if pokemon: 
        pokedex[pokemon["name"]] = pokemon
        print(f"{pokemon['name']} added to Pokédex.")
        print("\nPokedex: \n")
        view_pokedex()
    else:
        print(f"{name} was not found. Could not add to Pokédex.")


def view_pokedex():
    """\nDisplay all collected Pokémon."""
    if pokedex:
        for name, details in pokedex.items():
            print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}, Types: {', '.join(details['types'])}")
    else:
        print("Your Pokédex is empty.")

def remove_pokemon(name):
    """\nRemove a Pokémon from the Pokédex."""
    if name.capitalize() in pokedex:
        del pokedex[name.capitalize()]
        print(f"{name.capitalize()} removed from Pokédex.")
        print("\nPokedex: \n")
        view_pokedex()
    else:
        print("Pokémon not found in your Pokédex.")

#<------------------------------TEST YOUR FUNCTIONS BELOW------------------------------>

def main():
    while True:
        print("\nPokédex Menu:")
        print("1. Search Pokémon")
        print("2. Add Pokémon to Pokédex")
        print("3. View Pokédex")
        print("4. Remove Pokémon")
        print("5. Exit")
        choice = input("Choose an option: \n")

        if choice == "1":
            name = input("\nEnter Pokemon name to search: \n")
            search_pokemon(name)
        elif choice == "2":
            name = input("\nEnter Pokémon name to add: \n")
            add_pokemon(name)
        elif choice == "3":
            view_pokedex()
        elif choice == "4":
            name = input("\nEnter Pokémon name to remove: \n")
            remove_pokemon(name)
        elif choice == "5":
            print("\nExiting Pokédex.\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()