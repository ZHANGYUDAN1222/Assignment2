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
