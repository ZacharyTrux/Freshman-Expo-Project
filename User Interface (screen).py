import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window

#Window.clearcolor = (1,1,1,1)
Window.size = (1000,800)

class StartScreen(Widget):
    def __init__(self, **kwargs):
        super(StartScreen,self).__init__(**kwargs)

      
            
class SensoryPianoApp(App):
    def build(self):
        return StartScreen()
    

if __name__ == "__main__":
    SensoryPianoApp().run()
    

