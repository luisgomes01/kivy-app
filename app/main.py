from kivymd.app import MDApp
from kivy.lang import Builder
#:import rgba kivy.utils.rgba
from bills import bills as ListItems
from kivymd.uix.list import OneLineListItem

KV="""
FloatLayout:
    MDTopAppBar:
        size_hint_y: 0.3
        pos_hint: {'center_x': 0.5, 'center_y': 1}
        MDLabel:
            text: "Clip App"
            color: rgba("#ffffff")
            font_size: 35
        
    TextInput:
        id: textSearchField
        color: rgba("#000000")
        size_hint_x: 0.8
        size_hint_y: 0.08
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        hint_text: 'Search'
        font_size: 25
        on_text: app.filter_text(textSearchField.text)

    MDList:
        id: box
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
"""

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
       self.loadItems(ListItems)

    def loadItems(self, lst):
        for it in lst:
            _it = OneLineListItem(
                text = it["text"]
            )
            self.root.ids.box.add_widget(_it)

    def filter_text(self, text):
        ListItems_filter = []
        if len(text) == 0:
            self.root.ids.box.clear_widgets()
            for it in ListItems:
                ListItems_filter.append(it)
            self.loadItems(ListItems_filter)
            return
        if len(self.root.ids.box.children) > 0:
            self.root.ids.box.clear_widgets()
            for it in ListItems:
                if text.upper() in it["text"].upper():
                    ListItems_filter.append(it)
            if len(ListItems_filter) > 0:
                self.loadItems(ListItems_filter)
                
MainApp().run()