

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

class LoginWindow(MDBoxLayout):
    pass
class LoginApp(MDApp):
    def build(self):
        return LoginWindow()

if __name__=="__main__":
    LoginApp().run()