from machine import Pin
from time import sleep
class Stepper:
    def __init__(self, steps, pin1, pin2, pin3, pin4):
        self.steps = steps
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.current_step = 0

        # Set all pins as output
        self.pin1.init(Pin.OUT)
        self.pin2.init(Pin.OUT)
        self.pin3.init(Pin.OUT)
        self.pin4.init(Pin.OUT)

        # Define the sequence of steps
        self.sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]

    def setRPM(self, rpm):
        self.delay = 60 / (self.steps * rpm*2) 
        print(self.steps * rpm)

    def step(self, steps):
        for i in range(steps):
            for step in self.sequence:
                self.pin1.value(step[0])
                self.pin2.value(step[1])
                self.pin3.value(step[2])
                self.pin4.value(step[3])
                self.current_step += 1
                sleep(self.delay)
                if self.current_step == self.steps:
                    self.current_step = 0
                    break
