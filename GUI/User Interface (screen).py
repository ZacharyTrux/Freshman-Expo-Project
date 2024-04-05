import kivy
from kivy.app import App
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
          
            
class SensoryPianoApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        kv = Builder.load_file("SensoryPiano.kv") 
        return kv
    

if __name__ == "__main__":
    SensoryPianoApp().run()
    
