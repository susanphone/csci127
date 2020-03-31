# -----------------------------------------------------
# CSCI 127, Lab 8
# March 12, 2020
# Susan McCartney
# -----------------------------------------------------

# Your solution goes here...


class MSUContact:
    """ MSUContact class"""

    def __init__(self, first_name, last_name, phone_number):
        """ A constructor method that sets first name, title, and phone number"""
        self.title = ""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def set_first_name(self, first_name):
        """ A setter method that returns the first name"""
        self.first_name = first_name

    def get_first_name(self):
        """A reader method that returns the first name"""
        return self.first_name

    def get_last_name(self):
        """A reader method that returns the last name"""
        return self.last_name

    def set_title(self, title):
        """ A writer method that sets the title"""
        self.title = title

    def get_line_number(self):
        """ A reader function that gets the last four digits of the phone number"""
        return self.phone_number[-4:]

    def get_phone_number(self):
        """ A reader method that returns the phone number"""
        return self.phone_number

    def print_entry(self):
        """A reader method that return an entry to print"""
        padded_title = self.title
        if padded_title != "":
            padded_title += " "

        full_name = padded_title + self.first_name + " " + self.last_name + " "
        print("{:30}{}".format(full_name, self.phone_number))

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------


def print_directory(contacts):
    print("MSU Contacts:")
    print("----------------------------------------")
    for person in contacts:
        person.print_entry()
    print("----------------------------------------\n")

# -----------------------------------------------------


def main():

    prof_892 = MSUContact("Daniel", "DeFrance", "406-994-1624")
    mascot = MSUContact("MSU", "Bobcat", "406-994-0000")
    director_CS = MSUContact("John", "Paxton", "406-994-5979")
    president = MSUContact("Waded", "Cruzado", "406-994-CATS")

    contacts = [prof_892, mascot, director_CS, president]
    print_directory(contacts)

    mascot.set_first_name("Champ")

    prof_892.set_title("Instuctor")
    director_CS.set_title("Director")
    president.set_title("President")

    print_directory(contacts)

    contact = prof_892
    print(contact.get_first_name() + "'s MSU phone line is",
          contact.get_line_number())

# -----------------------------------------------------


main()
