from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout

class SignWindow(MDBoxLayout):
    pass
class SignApp(MDApp):
    def build(self):
        return SignWindow()

if __name__ == "__main__":
    SignApp().run()
