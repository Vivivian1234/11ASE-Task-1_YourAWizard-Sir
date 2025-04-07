from Spellbook import*


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