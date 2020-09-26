"""
CP1404 Assignment 2
class for multiple places
"""
import csv
from operator import itemgetter
# Create your PlaceCollection class in this file


class PlaceCollection:
    """Represent operations to multiple places"""

    def __init__(self):
        self.places_list = []

    def __str__(self):
        output = ''
        for perplace in self.places_list:
            for i in perplace[:-1]:
                output += str(i) + ','
            output = output + '\n'
        return output

    def load_places(self, filename):
        """Return a list of unvisited and visited places"""

        # Read file, and add data in dictionary
        try:
            with open(filename, 'r') as in_file:
                places_detail = in_file.readlines()
                for perplace in places_detail:
                    perplace = perplace.strip().split(',')
                    self.places_list.append(perplace)
                for i in self.places_list:
                    i[2] = int(i[2])

        except IOError:
            print('File not found.')
        # Test if the places are sorted correctly
        # print(self.places_list)

        return self.places_list

    def save_places(self, filename):
        """Store final data to the csv file"""

        # open the csv file in write mode
        with open(filename, 'w', newline='') as w_f:
            writer = csv.writer(w_f)
            writer.writerows(self.places_list)

    def add_place(self, place):
        """Add a new place to self.places_list"""
        self.places_list.append([place.name, place.country, place.priority, place.v_status])

    def num_nplaces(self):
        """Return a number of unvisited places"""

        num = 0
        for i in self.places_list:
            if i[3] == 'n':
                num += 1
            else:
                pass
        return num

    def sort_places(self,key='visited'):
        """Return a sorted list by priority"""

        # sort places order by 'n'(unvisited) then 'v'(visited) then priority
        if key.strip().upper() == 'VISITED':
            key = 3
        elif key.strip().upper() == 'PRIORITY':
            key = 2
        elif key.strip().upper() == 'COUNTRY':
            key = 1
        elif key.strip().upper() == 'NAME':
            key = 0
        self.places_list = sorted(self.places_list, key= itemgetter(key, 2))

        return self.places_list

    def list_places(self, key='visited'):
        """List places in list"""
        num = 1
        for i in self.sort_places(key):
            if i[3] == 'n':
                print('*{}. {:10} in {:13} priority {}'.format(num, i[0], i[1], i[2]))
                num += 1
            else:
                print(' {}. {:10} in {:13} priority {}'.format(num, i[0], i[1], i[2]))
                num += 1
        print('{} places. You still want to visit {} places.'.format(num-1, self.num_nplaces()))

