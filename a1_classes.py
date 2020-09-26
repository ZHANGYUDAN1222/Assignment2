"""
CP1404 Assignment 2
copy of Assignment 1
"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from placecollection import PlaceCollection

def main():
    """Run the whole process"""
    print("Travel Tracker 1.0 - by <Yudan Zhang>")
    place_collection = PlaceCollection()

    placs_list = place_collection.load_places('places.csv')

    while True:
        choice = read_menu()
        if choice == 'L':
            place_collection.list_places()

        elif choice == 'A':
            new_place = add_places()
            place_collection.add_place(Place(new_place[0], new_place[1], new_place[2], new_place[3]))

        elif choice == 'M':
            mark_places(place_collection, placs_list)

        elif choice == 'Q':
            print("""{} places saved to places.csv
Have a nice day :)""".format(len(place_collection.places_list)))
            break

        else:
            print("Invalid menu choice")

def read_menu():
    """Return the choice of menu"""

    choice = input("""Menu；
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
    return choice



if __name__ == '__main__':
    main()

