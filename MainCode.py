##################################################################################
# Project: Sensory Piano
# Group Members: Justus Blanchard, Grayson Lessard, Alayna Fields, Zachary Truxillo
##################################################################################
### SETUP ###
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import serial

Notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","C"]
keys_dict = {num_keys: Notes[num_keys] for num_keys in range(0,12)}

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
        
        actual_window = kv.get_screen("second")
        
        button = 
        self.action()
        
        def action(self):
            for num_key,notes in keys_dict:
                if(button == num_key):
                    actual_window.ids.notes_text_label.text = f"{notes}"
        
    
      
        
        
        return kv
    
### MAIN ###
# Start the app(GUI)
if __name__ == "__main__":
    SensoryPianoApp().run()

    
