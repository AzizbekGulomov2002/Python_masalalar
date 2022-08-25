from kivy.app import App
from kivy.uix.gridlayout import GridLayout
class MainWindow(GridLayout):
    pass
class MainApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    main = MainApp()
    main.run()