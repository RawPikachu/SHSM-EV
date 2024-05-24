from motor import Motor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

motor = Motor()
motor.start()

while True:
    