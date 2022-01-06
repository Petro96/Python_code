from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty



class MainApp(MDApp):

    dropdown = ObjectProperty()

    def on_start(self): 

        self.dropdown = MDDropdownMenu()

        # add items
        self.dropdown.items.append(
            {"viewclass":"MDMenuItem",
            "text":"Option 1",
            "callback":self.option_callback
            }
        )

    def option_callback(self,text):
        print(text)


MainApp().run()