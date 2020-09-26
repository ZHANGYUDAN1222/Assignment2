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
        self.root = Builder.load_file('TravelTracker.kv')
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


if __name__ == '__main__':
    TravelTrackerApp().run()
