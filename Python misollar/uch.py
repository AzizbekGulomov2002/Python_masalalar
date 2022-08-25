from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout

class UchWindow(FloatLayout):  
    pass
class UchApp(App):
    def build(self):
        return UchWindow()

if __name__=="__main__":
    Ikki = UchApp()
    Ikki.run()    