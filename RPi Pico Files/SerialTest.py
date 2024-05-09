##### SETUP #####
from machine import UART, Pin
import time

# Initialize UART on Raspberry Pi Pico
uart = UART(0, baudrate = 115200, tx=Pin(0), rx=Pin(1))
uart.init()

led = Pin(25, Pin.OUT)

##### MAIN #####
try:
    while True:
        # Send data over serial
        uart.write("Hello!".encode('utf-8'))
        print(";)")
        time.sleep(1)
        led.toggle()
        
except KeyboardInterrupt:
    uart.deinit() # Cleanup UART on exit
