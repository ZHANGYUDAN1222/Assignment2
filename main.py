"""
Name: Yudan Zhang
Date: 24/9/2020
Brief Project Description: an application to add new place and mark visited and unvisited places.
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-ZHANGYUDAN1222
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty

from placecollection import PlaceCollection

KEYs = {'Visited': 3, 'Priority': 2, 'Country': 1, 'Name': 0}

class TravelTrackerApp(App):
    """Create the application from App"""
    current_key = StringProperty()
    key_codes = ListProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')

    def build(self):
        """Build the Kivy GUI"""
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.key_codes =KEYs.keys()
        self.current_key = self.key_codes[0]
        self.create_widgets()

        return self.root

    def change_key(self, key):
        """ handle change of spinner selection, output result to label widget """
        self.clear_all()
        # print('change to:',key, KEYs[key])
        self.create_widgets(key)

    def add_place(self):
        """Add new place to GUI"""
        new_name = self.root.ids.new_name.text
        new_country = self.root.ids.new_country.text
        new_priority = self.root.ids.new_priority.text

        if new_name.strip() == '' or new_country.strip() == '' or new_priority.strip() == '':
            terminal = 'All fields must be completed'
        else:
            try:
                new_priority = int(new_priority)
            except ValueError:
                terminal = 'Please enter a valid number'
            else:
                if int(new_priority) <= 0:
                    terminal = 'Priority must be > 0'
                else:
                    terminal = '{} in {}, priority {} added.'.format(new_name, new_country, new_priority)
                    self.place_collection.places_list.append([new_name, new_country, int(new_priority), 'n'])

                    # print(new_name, new_country, new_priority)
                    new_btn = Button(id= new_name, text= '{} in {}, priority {} '.format(new_name, new_country, int(new_priority)))
                    self.root.ids.places_detail.add_widget(new_btn)
        self.root.ids.terminal.text = terminal
        self.clear_all()
        self.create_widgets()
        return self.place_collection.places_list

    def create_widgets(self, key='Visited'):
        """Create buttons from dictionary entries and add them to the GUI."""
        self.clear_all()
        self.place_collection.sort_places(key)
        self.num_nplaces()
        for places in self.place_collection.places_list:
            if places[3] == 'n':
                visit_status = ''
                bkcolor = (1, 0.61, 0.61, 1)
            else:
                visit_status = '(visited)'
                bkcolor = (0.3,0.4,0.4,1)
            place_string = '{} in {}, priority {} {}'.format(places[0], places[1], places[2], visit_status)
            place_btn = Button(id= places[0], text= place_string,background_color= bkcolor)
            self.root.ids.places_detail.add_widget(place_btn)
            place_btn.bind(on_release = self.change_status)

    def clear_btn(self):
        """Bind to clear button, clear all input"""
        self.root.ids.new_name.text = ''
        self.root.ids.new_country.text = ''
        self.root.ids.new_priority.text = ''
        self.root.ids.terminal = ''

    def change_status(self, instance):
        """When press button of place, change it visit status"""
        for place in self.place_collection.places_list:
            placestring = '{} in {}, priority {}'.format(place[0], place[1], place[2])
            if placestring.strip() == instance.text.replace('(visited)', '').strip():
                if place[3] == 'v':
                    if place[2] <= 2:
                        terminal = 'You need to visit {}. Get going!'.format(place[0])
                    else:
                        terminal = 'You need to visit {}.'.format(place[0])
                    place[3] = 'n'
                else:
                    if place[2] <= 2:
                        terminal = 'You visited {}, Great travelling!'.format(place[0])
                    else:
                        terminal = 'You visited {}.'.format(place[0])
                    place[3] = 'v'
                self.root.ids.terminal.text = terminal
            self.clear_all()
            self.create_widgets()

    def clear_all(self):
        """Clear all places buttons"""
        self.root.ids.places_detail.clear_widgets()

    def num_nplaces(self):
        """Return number of unvisited places"""
        n_place = self.place_collection.num_nplaces()
        self.root.ids.nplace.text = "Places to visit: {}".format(n_place)

    def on_stop(self):
        """Save all places when closing the app"""
        self.place_collection.save_places('places.csv')


if __name__ == '__main__':
    TravelTrackerApp().run()
