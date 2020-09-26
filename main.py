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


if __name__ == '__main__':
    TravelTrackerApp().run()
