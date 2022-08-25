from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

class LoginmdWindow(MDBoxLayout):
    pass
class LoginmdApp(MDApp):
    def build(self):
        return LoginmdWindow()

if __name__ == "__main__":
    LoginmdApp().run()
