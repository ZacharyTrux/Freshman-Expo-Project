##### SETUP #####
import time
from machine import Pin, PWM, Timer, UART
# The Base Frequency for all notes(motors 1-13) are set on the middle C octave on program launch.
# Base Frequencies are multiplied by 100 for optimal vibrational feel.

# UART init. for communication between Pico and RPi.
# Insures that the GUI will know which buttons are being pressed
# at any given instance.
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
uart.init()
    
# LED
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

#timer.init(freq = 2, mode = Timer.PERIODIC, callback = blink)

# Middle C (C)
motor1 = PWM(8, freq = 261000, duty_u16 = 0)
switch1 = Pin(2, Pin.IN, Pin.PULL_UP)

# C#/Db has been rewired directly to the RPi due to
# one PWM short on the Pico. Skibidi!
motor2 = PWM(8, freq = 261000, duty_u16 = 0)
switch2 = Pin(2, Pin.IN, Pin.PULL_UP)

# D
motor3 = PWM(10, freq = 293000, duty_u16 = 0)
switch3 = Pin(4, Pin.IN, Pin.PULL_UP)

# D#
motor4 = PWM(11, freq = 311000, duty_u16 = 0)
switch4 = Pin(5, Pin.IN, Pin.PULL_UP)

# E
motor5 = PWM(12, freq = 329000, duty_u16 = 0)
switch5 = Pin(6, Pin.IN, Pin.PULL_UP)

# F
motor6 = PWM(13, freq = 349000, duty_u16 = 0)
switch6 = Pin(7, Pin.IN, Pin.PULL_UP)

# F#/Gb
motor7 = PWM(9, freq = 369000, duty_u16 = 0)
switch7 = Pin(19, Pin.IN, Pin.PULL_UP)

# G
motor8 = PWM(3, freq = 391000, duty_u16 = 0)
switch8 = Pin(20, Pin.IN, Pin.PULL_UP)

# G#/Ab
motor9 = PWM(15, freq = 415000, duty_u16 = 0)
switch9 = Pin(21, Pin.IN, Pin.PULL_UP)

# A
motor10 = PWM(14, freq = 440000, duty_u16 = 0)
switch10 = Pin(22, Pin.IN, Pin.PULL_UP)

# A#/Bb
motor11 = PWM(16, freq = 466000, duty_u16 = 0)
switch11 = Pin(26, Pin.IN, Pin.PULL_UP)

# B
motor12 = PWM(17, freq = 493000, duty_u16 = 0)
switch12 = Pin(27, Pin.IN, Pin.PULL_UP)

# C
motor13 = PWM(18, freq = 523000, duty_u16 = 0)
switch13 = Pin(28, Pin.IN, Pin.PULL_UP)

# Lists needed to iterate in the main loop. Responsible for checking each
# button and motor.
motorList = [motor1, motor2, motor3, motor4, motor5, motor6, motor7, motor8, motor9, motor10, motor11, motor12, motor13]
switchList = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13]

##### MAIN #####
#Below are the controls that link the button inputs to its respective motor.
try:
    while True:

        for i in range(0, 13):
            for motor in motorList:
                if i != 1:
                    if switchList[i].value() == 0:
                        motorList[i].duty_u16(32768)
                    
                    # Communicate to RPi what button(s) are being pressed.
                        buttonPressed = str(i) + "\n"
                        
                        # print(buttonPressed)
                        
                        # Send information across wires via UART.
                        uart.write(str(buttonPressed).encode('utf-8'))
                        
                        # blink LED as long as this function executes
                        led.toggle()
                    else:
                        # Turn off motor when not pressed.
                        motorList[i].duty_u16(0)
                    
except KeyboardInterrupt:
    uart.deinit()
