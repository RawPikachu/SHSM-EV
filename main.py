from time import sleep
from motor import Motor
import RPi.GPIO as GPIO
import threading


GPIO.setmode(GPIO.BCM)
GPIO.setup((17, 27, 22, 23), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

motor = Motor()
motor.start()

log_count = 0
duty_cycle = 0


def input_loop():
    global log_count, duty_cycle

    while True:
        if GPIO.input(17):
            motor.stop_running = False
            if GPIO.input(27):
                if GPIO.input(22):
                    if GPIO.input(23):
                        duty_cycle = 0.8
                    else:
                        duty_cycle = 0.6
                else:
                    duty_cycle = 0.4
            else:
                duty_cycle = 0.2
        else:
            motor.stop_running = True
            motor.duty_cycle = 0

        if log_count % 100 == 0:
            print(f"Current Duty Cycle: {motor.duty_cycle}")

        log_count += 1
        sleep(0.01)


threading.Thread(target=input_loop).start()

while True:
    motor.ramp_duty_cycle(duty_cycle)
    sleep(0.01)
