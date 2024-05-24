from time import sleep
from motor import Motor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup((17, 27, 22, 23), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

motor = Motor()
motor.start()

log_count = 0

while True:
    if GPIO.input(17):
        motor.stop_running = False
        if GPIO.input(27):
            if GPIO.input(22):
                if GPIO.input(23):
                    motor.ramp_duty_cycle(0.8)
                else:
                    motor.ramp_duty_cycle(0.5)
            else:
                motor.ramp_duty_cycle(0.25)
        else:
            motor.ramp_duty_cycle(0.1)
    else:
        motor.stop_running = True
        motor.ramp_duty_cycle(0)

    if log_count % 10 == 0:
        print(f"Current Duty Cycle: {motor.duty_cycle}")

    log_count += 1
    sleep(0.1)
