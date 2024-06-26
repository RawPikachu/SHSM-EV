import pyvesc
import threading
from time import sleep


class Motor:
    def __init__(self, acceleration: float = 0.012, serial_port: str = "/dev/ttyAMA0"):
        self.serial_port = serial_port
        self.vesc = pyvesc.VESC(self.serial_port, start_heartbeat=False)
        self.duty_cycle = 0
        self.acceleration = acceleration
        self.loop_thread = threading.Thread(target=self.update_loop)
        self.active = False
        self.stop_running = False

    def update_loop(self):
        while True:
            self.vesc.set_duty_cycle(self.duty_cycle)

    def start(self):
        self.vesc.start_heartbeat()
        self.active = True
        self.loop_thread.start()

    def stop(self):
        self.vesc.stop_heartbeat()
        self.active = False
        self.loop_thread.join()

    def ramp_duty_cycle(self, target: float):
        if target == 0:
            self.duty_cycle = 0
            return

        while abs(self.duty_cycle - target) > self.acceleration:
            if self.stop_running:
                self.duty_cycle = 0
                return
            if target > self.duty_cycle:
                self.duty_cycle += self.acceleration
            else:
                self.duty_cycle -= self.acceleration
            sleep(0.01)

        if self.stop_running:
            self.duty_cycle = 0
            return
        self.duty_cycle = target
