import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class StartScreen(Screen):
    #in the event we need to have this for touch screen
    #def on_touch_down(self,touch):
    pass

class ActualWindow(Screen):
    pass    
    
class WindowManager(ScreenManager):
    pass

        
kv = Builder.load_file("SensoryPiano.kv")      
            
class SensoryPianoApp(App):
    def build(self):
        #Window.clearcolor = (1,1,1,1)
        return kv
    

if __name__ == "__main__":
    SensoryPianoApp().run()
    

