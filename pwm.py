from rpi_hardware_pwm import HardwarePWM

pwm = HardwarePWM(pwm_channel=0, hz=50, chip=0)
pwm.start(7.5)

input("Press Enter to stop the PWM signal")

pwm.stop()
