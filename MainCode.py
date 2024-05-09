##### SETUP #####
# General imports; Communication, music, and GPIO
import serial
import pygame
import RPi.GPIO as GPIO

# KIVY imports
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock


# Setup motor2 and button2
motorPin = 13
buttonPin = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(motorPin, GPIO.OUT)
motor2 = GPIO.PWM(motorPin, 277000)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Duty cycle for motor2
motor2.start(0)

# Constant serial port for serial communication
SERIAL_PORT = '/dev/ttyAMA0'

# Initialize pygame.mixer and channels for sound output
pygame.mixer.init()
pygame.mixer.set_num_channels(13)

channelDict = {}

for i in range(0, 13):
    channelDict[i] = pygame.mixer.Channel(i)

# Setup note list and key dictionary
notesList = ["C4", "C#4/Db4", "D4","D#4/Eb4", "E4", "F4", "F#4/Gb4", "G4", "G#4/Ab4", "A4", "A#4/Bb4", "B4", "C5"]

keys_dict = {num_keys: notesList[num_keys] for num_keys in range(0, 13)}

class StartScreen(Screen):
    pass

class ActualWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass 

class SensoryPianoApp(App):
    def build(self):
        # Create and update the window
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1024, 600)
        Window.fullscreen = 'auto'
        
        kv = Builder.load_file('sensorypiano.kv')
        
        global actual_window
        actual_window = kv.get_screen('second')

        # Set the timer for redrawing the screen
        refreshTime = 0.02
        Clock.schedule_interval(self.timer, refreshTime)
        
        return kv

    # Function responsible for iterating through a loop. Updates window,
    # gets information, displays text, and plays sound.
    def timer(self, dt):
        global actual_window

        # Get data from serial port    
        receivedData = pico.readline()
        receivedData = receivedData.decode()
        receivedData = receivedData.strip()
        # print(receivedData)
        
        # Get button2 input state. If pressed, turn on motor2.
        # If not pressed, turn it off.
        input_state = GPIO.input(19)

        if input_state == False:
            receivedData = 1
            motor2.ChangeDutyCycle(50)
        else:
            motor2.ChangeDutyCycle(0)
            


        # Updates GUI with cooresponding note for each key (button)
        try:
            # Retrieve sent information from Pico
            buttonNum = int(receivedData)
            noteFromData = str(keys_dict[buttonNum])
            noteFromData = noteFromData.replace('/', '')
            # print(noteFromData)

            actual_window.ids.notes_text_label.text = f"{keys_dict[buttonNum]}"

            # Play note corresponding to key pressed
            if channelDict[buttonNum].get_busy() == False:
                noteToPlay = keys_dict[buttonNum]
                noteToPlay = noteToPlay.replace("/", "")
                # print(noteToPlay)
                note = pygame.mixer.Sound(f"notes/{noteToPlay}.wav")
                channelDict[buttonNum].play(note)

        except:
            pass


##### MAIN #####
if __name__ == "__main__":
    try:
        # If possible, open a serial port to the Pico.
        pico = serial.Serial(SERIAL_PORT, 115200, timeout=0.01)
    except:
        # Alert the user upon failure.
        print("Failed to connect.")
        exit()

    # Launch the app
    SensoryPianoApp().run()

    # Close serial communication
    pico.close()
