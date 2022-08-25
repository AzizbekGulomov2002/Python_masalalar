from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
class FormWindow(FloatLayout):
    pass
class FormApp(App):
    def build(self):
        return FormWindow()

if __name__=="__main__":
    Ikki = FormApp()
    Ikki.run()    