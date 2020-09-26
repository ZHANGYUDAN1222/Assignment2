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

class TravelTrackerApp(App):
    """..."""
    pass


if __name__ == '__main__':
    TravelTrackerApp().run()
