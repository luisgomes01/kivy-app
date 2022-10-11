from kivymd.app import MDApp
from kivy.lang import Builder


KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
    BoxLayout:
        size_hint: 0.7, 0.08
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        TextInput:
            halign: "center" 
            hint_text: 'Search'
            font_size: 25
    

'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()