import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Susan McCartney                       |
# Last Modified: April 3, 2019          |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class Pokemon:
    """Base class for any animated creature from Pokemon"""
    def __init__(self, name, number, combat_points, types):
        self.pokemon_name = name
        self.pokemon_number = number
        self.combat_points = combat_points
        self.pokemon_type = types
    
    def get_name(self, name):
        self.pokemon_name = name
    
    def get_number(self, number):
        self.pokemon_number = number
    
    def get_combat_points(self, combat_points):
        self.combat_points = combat_points
    
    def get_types(self, types):
        self.pokemon_type = types

def lookup_by_name(self, name, pokedex):  #getters
        name = pokedex.get
        return self.name
    
def lookup_by_number(self, number, pokedex): #getters
        number = pokedex.get
        return self.number
    
def total_by_type(self, pokemon_type, pokedex):
        pokemon_type = pokedex.get
        return self.types
    
def average_hit_points(self, combat_points, pokedex):
        combat_points = pokedex.get
        return self.combat_points

def print_menu():
    print("""
    1. Print Pokedex
    2. Print Pokemon by Name
    3. Print Pokemon ny Number
    4. Count Pokemon with Type
    5. Print Average Pokemon Combat Points
    6. Quit
    """)


def print_pokedex(pokedex):
    pass
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------


def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------


def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------


def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------


main()
