from asyncio import sleep, run
from motor import Motor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup((17, 27, 22, 23), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

motor = Motor()
motor.start()

log_count = 0


async def main():
    while True:
        if GPIO.input(17):
            motor.stop_running = False
            if GPIO.input(27):
                if GPIO.input(22):
                    if GPIO.input(23):
                        await motor.ramp_duty_cycle(0.8)
                    else:
                        await motor.ramp_duty_cycle(0.5)
                else:
                    await motor.ramp_duty_cycle(0.25)
            else:
                await motor.ramp_duty_cycle(0.1)
        else:
            motor.stop_running = True
            motor.duty_cycle = 0

        if log_count % 100 == 0:
            print(f"Current Duty Cycle: {motor.duty_cycle}")

        log_count += 1
        sleep(0.01)


run(main())
