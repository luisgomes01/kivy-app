
import kivy
kivy.require('2.1.0')
from kivy.app import App 

class searchBar(App):
    pass

class Main(App):
    def build(self):
        return searchBar()

searchBar().run()