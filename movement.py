from adafruit_servokit import ServoKit
import time


kit = ServoKit(channels=16)


def move_servos(angle1):
    kit.servo[0].angle = angle1


try:
    while True:
        move_servos(0)
        move_servos(45)
        move_servos(90)
        move_servos(180)
except KeyboardInterrupt:
    print("Program stopped")

finally:
    move_servos(90)
