import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window

Window.size = (1000,800)

class StartScreen(ButtonBehavior,Label,FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen,self).__init__(**kwargs)
        Window.clearcolor = (1,1,1,1)
        with self.canvas:
            Color(0,0,0,0)
            Rectangle(pos=1,size=5)
        
      
            
class SensoryPianoApp(App):
    def build(self):
        return StartScreen()
    

if __name__ == "__main__":
    SensoryPianoApp().run()
    
