from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout

class loginWindow(FloatLayout):
    pass
class loginApp(App):
    def build(self):
       return loginWindow()
if __name__ == "__main__":
        log = loginApp()
        log.run()