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
    pass

class ActualWindow(Screen):
    pass    
    
class WindowManager(ScreenManager):
    pass
          
class SensoryPianoApp(App):
    def build(self):
        # Sets the background of the screen to White 
        Window.clearcolor = (1,1,1,1)
        Window.size = (1024,600)
        # Loads the kv file which contains all of the buttons, labels, and functions (utilizes kivy lang)
        kv = Builder.load_file("SensoryPiano.kv") 
        return kv
    

### MAIN ###
# Start the app(GUI)
if __name__ == "__main__":
    SensoryPianoApp().run()
    
