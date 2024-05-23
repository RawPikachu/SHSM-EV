import pyvesc
import threading


class Motor:
    def __init__(
        self, serial_port: str = "/dev/ttyACM0"
    ):  # The default port is different on RPI, most likely /dev/ttyUSBX, where X is a number
        self.serial_port = serial_port
        self.vesc = pyvesc.VESC(self.serial_port, start_heartbeat=False)
        self.duty_cycle = 0
        self.loop_thread = threading.Thread(target=self.update_loop)
        self.active = False

    def update_loop(self):
        last_cycle = self.duty_cycle
        while True:
            if self.duty_cycle != last_cycle:
                self.vesc.set_duty_cycle(self.duty_cycle)
            last_cycle = self.duty_cycle

    def start(self):
        self.vesc.start_heartbeat()
        self.active = True
        self.loop_thread.start()

    def stop(self):
        self.vesc.stop_heartbeat()
        self.active = False
        self.loop_thread.join()

    # TODO: Implement this
    def ramp_duty_cycle(self, target: float, time: float):
        start = self.duty_cycle
        step = (target - start) / time
        while self.duty_cycle < target:
            self.duty_cycle += step
            time.sleep(1)
        self.duty_cycle = target
