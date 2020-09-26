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
            new_place = validate_new_places()
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

def validate_new_places():
    """Add new place to place object"""
    f_new_name = True  # set look key word for place name

    while f_new_name:
        try:
            new_name = input('Name:')
            if new_name.strip() == '':
                raise IndexError
            else:
                f_new_name = False
                f_new_country = True  # set loop key word for country
        except IndexError:
            print('Input cannot be blank')

    while f_new_country:
        try:
            new_country = input('Country:')
            if new_country.strip() == '':
                raise IndexError
            else:
                f_new_country = False
                f_new_priority = True  # set loop key word for priority
        except IndexError:
            print('Input cannot be blank')

    while f_new_priority:
        try:
            new_priority = input('Priority:')
            if new_priority.strip() == '':
                raise IndexError
            elif new_priority.isdigit() == 'False':
                raise ValueError
            elif int(new_priority) <= 0:
                print('Number must be > 0')
            else:
                print('{} in {} (priority {}) added to Travel Tracker'.format(new_name, new_country, new_priority))
                new_place = [new_name, new_country, int(new_priority), False]
                return new_place
                f_new_priority = False

        except IndexError:  # if input is blank, loop again
            print('Input cannot be blank')

        except ValueError:  # if input is not a number, loop again
            print('Invalid input; enter a valid number')

def mark_places(place_collection, places_list):
    """Return a list with changes in visited and unvisited places"""
    nnum = place_collection.num_nplaces()
    if nnum == 0:
        print('No unvisited places')
    else:
        place_collection.list_places()
        print('Enter the number of a place to mark as visited')

        while True:
            change = input('>>>')
            if change.strip() == '':
                print('Input cannot be blank')
            elif change.isdigit() == 'False':
                print('Invalid input; enter a valid number')
            elif int(change) < 0:
                print('Number must be > 0')
            elif int(change) > len(places_list):
                print('Invalid place number')
            elif places_list[int(change) - 1][3] == 'v':
                print('That place is already visited')
            else:
                places_list[int(change) -1][3] = 'n'
                break
        return places_list



if __name__ == '__main__':
    main()

