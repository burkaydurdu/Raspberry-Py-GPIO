import RPi.GPIO as GPIO
import time


ledRight = 14
ledMid = 18
ledLeft = 21


GPIO.setmode(GPIO.BCM)

GPIO.setup(ledRight, GPIO.OUT)
GPIO.setup(ledMid, GPIO.OUT)
GPIO.setup(ledLeft, GPIO.OUT)


while TRUE:
    time.sleep(0.075)
    GPIO.output(ledLeft, GPIO.HIGH)
    time.sleep(0.075)
    GPIO.output(ledMid, GPIO.HIGH)
    time.sleep(0.075)
    GPIO.output(ledRight, GPIO.HIGH)
    time.sleep(0.075)
    GPIO.output(ledRight, GPIO.LOW)
    time.sleep(0.075)
    GPIO.output(ledMid, GPIO.LOW)
    time.sleep(0.075)
    GPIO.output(ledLeft, GPIO.LOW)

GPIO.cleanup()
