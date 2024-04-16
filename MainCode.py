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
        
        # GPIO.setmode(GPIO.BCM)
        # button_pin = 18  # Change this to your button's GPIO pin
        # GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.add_event_detect(button_pin, GPIO.FALLING, \
        #     callback=self.button_callback, bouncetime=300)
        window = self.root.get_screen("second")
        window.ids.octave_text_label.text = "Button Pressed"
        return kv
    
    def button_callback(self, channel):
        # updates label under notes and octave when pressed
        window = self.root.get_screen("second")
        window.ids.octave_text_label.text = "Button Pressed"
        window.ids.notes_text_label.text = "Button Pressed"
    
### MAIN ###
# Start the app(GUI)
if __name__ == "__main__":
    SensoryPianoApp().run()