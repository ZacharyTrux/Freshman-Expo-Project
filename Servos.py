import RPi.GPIO as GPIO

MIN_DUTY = 5
MAX_DUTY = 10

servo_signal_pin = 13

def deg_to_duty(deg):
    return (deg - 0) * (MAX_DUTY - MIN_DUTY) / 180 + MIN_DUTY

if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(servo_signal_pin, GPIO.OUT)
    #set PWM signal to 50Hz
    servo = GPIO.pwm(servo_signal_pin, 50)
    servo.start(0)

    #loops from 0 to 180
    for deg in range(181):
        duty_cycle = deg_to_duty(deg)
        servo.ChangeDutyCycle(duty_cycle)

    #cleanup the gpio pins
    GPIO.cleanup()
    #HELLO
