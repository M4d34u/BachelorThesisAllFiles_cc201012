import RPi.GPIO as GPIO

relay_pins = [4, 17, 2, 3]
ON = False
OFF = True

def init():
    GPIO.setmode(GPIO.BCM)
    for pin in relay_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, OFF)

def power(is_on):
    for pin in relay_pins[2:]:
        GPIO.output(pin, is_on)

def cool():
    power(ON)
    for pin in relay_pins[:2]:
        GPIO.output(pin, OFF)

def heat():
    power(ON)
    for pin in relay_pins[:2]:
        GPIO.output(pin, ON)

def off():
    power(OFF)

modes = {
    'HEAT': heat,
    'COOL': cool,
    'OFF': off
}

def set_mode(mode):
    modes[mode]()

def gpiocleanup():
    GPIO.cleanup()
