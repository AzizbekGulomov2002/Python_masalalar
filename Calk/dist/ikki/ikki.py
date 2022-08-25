from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class IkkiWindow(BoxLayout):
    inp = ObjectProperty()
    def hisob(self, a):       
        if a == "+":
            self.son = float(self.inp.text)
            self.t = a
            self.inp.text = ""
        elif a == "-":
            self.son = float(self.inp.text)
            self.t = a
            self.inp.text = ""
        elif a == "/":
            self.son = float(self.inp.text)
            self.t = a
            self.inp.text = ""
        elif a == "=":

            if self.t == "+":
                self.son1 = float(self.inp.text)
                self.inp.text = str(self.son+self.son1)
            elif self.t == "-":
                self.son1 = float(self.inp.text)
                self.inp.text = str(self.son-self.son1)
            elif self.t == "*":
                self.son1 = float(self.inp.text)
                self.inp.text = str(self.son*self.son1)
  
            elif self.t == "/":
                self.son1 = float(self.inp.text)
                self.inp.text = str(self.son/self.son1)
            elif self.t == "%":
                self.son1 = float(self.inp.text)
                self.inp.text = str(self.son*self.son1/100)
                  
               
        elif a == "<":
            self.n = ""
            m = list(self.inp.text)
            for i in range(len(m)-1):
                self.n+=m[i]
            self.inp.text = self.n
            
        elif a == "%":
            self.son = float(self.inp.text)
            self.t = a
            self.inp.text = ""   


        elif a == "c":
            self.inp.text = ""
        elif  a == "*": 

            self.son = float(self.inp.text)
            self.t = a
            self.inp.text = ""
                      
        else:
            self.inp.text += a
    
class IkkiApp(App):
    def build(self):
        return IkkiWindow()

if __name__=="__main__":
    Ikki = IkkiApp()
    Ikki.run()    
    