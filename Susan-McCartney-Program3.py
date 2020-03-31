# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Classics CSV Library          |
# Susan McCartney                          |
# Last Modified: March 13, 2020            |
# -----------------------------------------+
# Using a menu list, take user's choice for|
# what option they want to navigate in the |
# menu. Create three functions that        |
# identify most popular books, difficulty  |
# range, and all book by a particular      |
# author. One function is also created     |
# on your own.                             |
# -----------------------------------------+
import string


def most_popular(input_file):
    file = open(input_file, "r")
    most_downloaded = 0
    title = ""
    for line in file:
        file_list = line.split(",")
        downloads = file_list[5]
        book_title = file_list[3]

        try:
            downloads = int(downloads)
        except ValueError:
            continue

        if downloads > most_downloaded:
            most_downloaded = downloads
            title = book_title

    print("The most popular download is " + title)
    file.close()


def fk_difficulty_range(input_file, least, most):
    file = open(input_file, encoding="ISO-8859-1")
    difficulties = []
    least = int(least)
    most = int(most)
    for line in file:
        file_list = line.split(",")
        difficulty = file_list[23]
        book_title = file_list[3]
        try:
            difficulty = float(difficulty)
        except ValueError:
            continue
        difficulties.append((difficulty, book_title))

    difficulties.sort()

    for i in range(least, most+1):
        print(str(i) + " - " + difficulties[i][1] +
              " - Grade Level: " + str(difficulties[i][0]))

    file.close()


def all_books_by_author(input_file, author):
    file = open(input_file)
    books = {}
    for line in file:
        file_list = line.split(",")
        auth = file_list[11]
        full_name = auth.split(" ")
        book = file_list[3]
        if full_name[0] == author:
            books[book] = auth
    for book in books:
        print(book + " by " + books[book])


def search_string(input_file, search):
    file = open(input_file)
    results = {}
    for line in file:
        file_list = line.split(",")
        genre = file_list[2]
        title = file_list[3]
        if search.lower() in genre.lower() or search.lower() in title.lower():
            results[title] = genre
    for key in results:
        print(results[key] + ": " + key, "\n")

    file.close()

# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+


def menu():
    print()
    print("1. Identify the most popular book download.")
    print("2. List a range of books by difficulty rating.")
    print("3. Identify all books by certain author.")
    print("4. Something interesting... Search!")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+


def main():
    input_file = "classics.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            most_popular(input_file)
        elif (choice == 2):
            least = input("Enter least difficult out of 1000 (e.g. 250): ")
            most = input("Enter most difficult out of 1000 (e.g. 300): ")
            print("Using the Flesch–Kincaid grade level formula.\n")
            fk_difficulty_range(input_file, least, most)
        elif (choice == 3):
            author = input("Enter last name of author (e.g. Dickens): ")
            all_books_by_author(input_file, author)
        elif (choice == 4):
            search = input(
                "Enter word that interests you. A book, an idea, a subject?: ")

            print("\n",  "Search results: ", "\n")
            search_string(input_file, search)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+


main()
