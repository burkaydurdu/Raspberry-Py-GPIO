import RPi.GPIO as GPIO
import time


ledPin = 14

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.HIGH)

time.sleep(0.075)
GPIO.cleanup()
