##################################################################################
# Project: Sensory Piano
# Group Members: Justus Blanchard, Grayson Lessard, Alayna Fields, Zachary Truxillo
##################################################################################
### SETUP ###
import pygame
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
# import piano

class StartScreen(Screen):
    #in the event we need to have this for touch screen
    #def on_touch_down(self,touch):
    pass

class ActualWindow(Screen):
    pass    
    
class WindowManager(ScreenManager):
    pass
          
            
class SensoryPianoApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        Window.size = (1024,600)
        kv = Builder.load_file("SensoryPiano.kv") 
        return kv
    

### MAIN ###
# Code
def thisThing():
    pass

if __name__ == "__main__":
    SensoryPianoApp().run()