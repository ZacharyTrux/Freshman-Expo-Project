import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

#Window.clearcolor = (1,1,1,1)
Window.size = (1000,800)

class StartScreen(FloatLayout):
    pass
    
#class ActualScreen(Widget):
 #   pass
        
      
            
class SensoryPianoApp(App):
    def build(self):
        #$sm = ScreenManager()
        #sm.add_widget(StartScreen(name='StartScreen'))
        #sm.add_widget(ActualScreen(name="ActualScreen"))
        
        return StartScreen()
    

if __name__ == "__main__":
    SensoryPianoApp().run()
    

