"""
1404 Assignment
class for functions of each place
"""

# Create your Place class in this file


class Place:
    """Represent a Place object"""

    def __init__(self, name='', country='', priority=0, v_status=''):
        """Initialise a place instance"""
        self.name = name
        self.country = country
        self.priority = priority
        self.v_status = v_status

        if self.v_status == False:
            self.v_status = 'n'
        elif self.v_status == True:
            self.v_status = 'v'

    def __str__(self):
        """Return string representation of place object"""
        return "{} in {} priority {}, visited = {}".format(self.name, self.country, self.priority, self.v_status)

    def mark_visited(self):
        """Return visited for unvisited place"""
        self.v_status = 'v'
        return self.v_status
