import time
from  RPi.GPIO import GPIO
from machine import Pin, PWM

motor1 = PWM(Pin(0))
motor1.freq(1000)

switch1 = Pin(1, Pin.IN, Pin.PULL_UP)

while True: #while switch1 == True:
    for i in range(0, 65535, 5):
        pwm1.dutyu16(i)
        time.sleep(0.001)

    print("100%")
    time.sleep(2)

    for i in range(65535, 0, 5):
        pwm1.duty_u16(i)
        time.sleep(0.001)

    print("100%")
    time.sleep(2)

GPIO.cleanup()
