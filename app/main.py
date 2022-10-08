import kivy
kivy.require('2.1.0')
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tasks(BoxLayout):
    def __init__(self, tasks):
        super().__init__()
        for task in tasks:
            self.add_widget(Label(text=task))


class Main(App):
    def build(self):
        return Tasks(['Go shopping', 'Go to college'])

Main().run()