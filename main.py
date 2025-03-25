import requests # Must import requests so we can use API

# API Base URL for HarryPotterSpellsAPI
API_URL = "http://hp-api.onrender.com/api/spells"

# Dictionary to store collected spells
spellbook = {}

def search_spell(name):
    """\nSearch for a spell by the name and return its details."""
    response = requests.get(f"{API_URL}?name={name}")
    if response.status_code == 200:
        data = response.json()

        matching_spells = [spell for spell in data if spell["name"].lower() == name.lower()]

        if matching_spells:  # If there's at least one spell that matches
            spell_info = {
                "name": matching_spells[0]["name"],  # Access the name of the matched spell
                "description": matching_spells[0]["description"]  # Access the description of the matched spell
            }
            
            return spell_info  # Return the spell's details
        
        else:
            print("\nSpell not found.")
            return None
    else:
        print(f"\nFailed to fetch data. Status code: {response.status_code}")
        return None




def add_spell(name):
    """\nAdd a spell to your spellbook."""
    spell = search_spell(name)  # Now we get the return value of search_spell
    if spell:
        spellbook[spell["name"]] = spell  # Add spell details to the spellbook
        print(f"{spell['name']} added to spellbook.")
        print("\nSpellbook: \n")
        view_spellbook()
    else:
        print(f"{name} was not found. Could not add to your spellbook.")

def view_spellbook():
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
        print("\nSpellbook: \n")
        view_spellbook()
    else:
        print("Spell not found in your spellbook.")

#<------------------------------TEST YOUR FUNCTIONS BELOW------------------------------>

def main():
    while True:
        print("\nSpellbook Menu:")
        print("1. Search spell")
        print("2. Add spell to spellbook")
        print("3. View spellbook")
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
            view_spellbook()
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