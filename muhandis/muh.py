from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout





class MuhWindow(MDBoxLayout):
    pass
class MuhApp(MDApp):
    def build(self):
        return MuhWindow()

if __name__ == "__main__":
    MuhApp().run()