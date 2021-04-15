import RPi.GPIO as GPIO #Importing GPIO library 
from time import sleep  # Importing sleep funtion from time

GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD) # setting up the mode
GPIO.setup(8, GPIO.OUT) # setting up the pin we want for our output as i use 8!

try:
    while:
        GPIO.output(8,GPIO.HIGH)
        sleep(0.25)
        GPIO.output(8, GPIO.LOW)
        sleep(0.25)
except KeyboardInterrupt:
    GPI.cleanup()