import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button

class StartScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen,self).__init__(**kwargs)
        
class BtnApp(App):
    def build(self):
        return StartScreen()
    
    
if __name__ == "__main__":
    BtnApp().run()