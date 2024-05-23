import pyvesc
import time

# Just run this for testing, motor.py is bad.

# The default port is different on RPI, most likely /dev/ttyUSBX, where X is a number
with pyvesc.VESC("/dev/ttyACM0") as vesc:
    while True:
        vesc.set_duty_cycle(0.8)
        # vesc.set_rpm(900)
        time.sleep(1)
