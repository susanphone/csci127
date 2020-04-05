import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Susan McCartney                       |
# Last Modified: April 3, 2019          |
# ---------------------------------------
# A Pokemon program that contains info
# about each Pokemon using a pokedex. This
# program gives you options via menu on
# where to navigate through the program.
# ---------------------------------------


class Pokemon:
    """Base class for any animated creature from Pokemon"""

    def __init__(self, name, number, combat_points, types):
        self.pokemon_name = name
        self.pokemon_number = number
        self.combat_points = combat_points
        self.pokemon_types = types

    def get_name(self):
        """Retrieves the Pokemon's name from the Pokemon class"""
        return self.pokemon_name

    def get_number(self):
        """Retrieves the Pokemon's number from the Pokemon class"""
        return self.pokemon_number

    def get_combat_points(self):
        """Retrieves the Pokemon's combat points from the Pokemon class"""
        return self.combat_points

    def get_types(self):
        """Retrieves the Pokemon's types from the Pokemon class"""
        return self.pokemon_types

    def print_pokemon(self):
        """Prints the credentials of each pokemon"""
        type_separator = " and "
        print("Number: %d, Name: %s, CP: %d, Type: %s" % (self.pokemon_number, self.pokemon_name.capitalize(
        ), self.combat_points, type_separator.join(self.pokemon_types)))


def lookup_by_name(pokedex, name):
    """Find the Pokemon's name in the Pokedex and return the info on that Pokemon"""
    for pokemon in pokedex:
        if pokemon.get_name() == name:
            pokemon.print_pokemon()
            return
    print("There is no Pokemon named " + name, end="")


def lookup_by_number(pokedex, number):
    """Find the Pokemon's number in the Pokedex and return the info on that Pokemon"""
    for pokemon in pokedex:
        if pokemon.get_number() == number:
            pokemon.print_pokemon()
            return
    print("There is no Pokemon number " + str(number), end="")


def total_by_type(pokedex, pokemon_type):
    """Find all the Pokemon with the type given by the user"""
    count = 0
    for pokemon in pokedex:
        if pokemon_type in pokemon.get_types():
            count += 1
    print("Number of Pokemon that contain type " +
          pokemon_type + " = " + str(count), end="")


def average_hit_points(pokedex):
    """Add up all the combat points of every Pokemon and find the average hit points"""
    total_cp = 0
    for pokemon in pokedex:
        total_cp += pokemon.get_combat_points()
    print("Average Pokemon combat points = " +
          str(round(total_cp/len(pokedex), 2)), end="")


def print_menu():
    """Print menu of options to choose from"""
    print("""
    1. Print Pokedex
    2. Print Pokemon by Name
    3. Print Pokemon by Number
    4. Count Pokemon with Type
    5. Print Average Pokemon Combat Points
    6. Quit
    """)


def print_pokedex(pokedex):
    """Print all the pokemon and their credentials"""
    for pokemon in pokedex:
        pokemon.print_pokemon()

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
