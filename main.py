import requests # Must import requests so we can use API

# API Base URL for HarryPotterSpellsAPI
API_URL = "https://hp-api.onrender.com/api/spells"

# Dictionary to store collected spells
spellbook = {}

def search_spell(name):
    """\nSearch for a spell by the name and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        spell_info = {
            "name": data["name"].capitalize(),
            "description": data["description"],
        }
        print(spell_info)
        
    else:
        print("\nSpell not found.")
        return None

def add_spell(name):
    """\nAdd a spell to your spellbook."""
    spell = search_spell(name)
    if spell:
        spellbook[spell["name"]] = spell
        print(f"{spell['name']} added to spellbook.")

def view_spell():
    """\nDisplay all collected spells."""
    if spellbook:
        for name, details in spellbook.items():
            print(f"{name} - Description: {details['description']}")
    else:
        print("Your spellbook is empty.")

def remove_spell(name):
    """\nRemove a spell from your spellbook."""
    if name.capitalize() in spellbook:
        del spellbook[name.capitalize()]
        print(f"{name.capitalize()} removed your spellbook.")
    else:
        print("Spell not found in your spellbook.")

#<------------------------------TEST YOUR FUNCTIONS BELOW------------------------------>

def main():
    while True:
        print("\nSpellbook Menu:")
        print("1. Search spell")
        print("2. Add spell to spellbook")
        print("3. View spell")
        print("4. Remove spell")
        print("5. Exit")
        choice = input("Choose an option: \n")

        if choice == "1":
            name = input("\nEnter spell name to search: \n")
            search_spell(name)
        elif choice == "2":
            name = input("\nEnter spell name to add: \n")
            add_spell(name)
        elif choice == "3":
            view_spell()
        elif choice == "4":
            name = input("\nEnter spell name to remove: \n")
            remove_spell(name)
        elif choice == "5":
            print("\nExiting spellbook.\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()