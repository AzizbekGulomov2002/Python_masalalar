from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout

class UyWindow(FloatLayout):  
    pass
class UyApp(App):
    def build(self):
        return UyWindow()

if __name__=="__main__":
    uy = UyApp()
    uy.run()    