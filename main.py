# Pillars
# Testing the movement of the pillars
from microbit import *
import random

class Pillars:
    brightness = 5
    MOVETIME = 500
    StartX = 4
    EndX = 1

    p1SafeY = 0
    p2SafeY = 1
    p3SafeY = 2
    p4SafeY = 3
    p5SafeY = 4

    display.clear()

    def __init__(self):
        pass

    def Go(self):
        sleep(100)
        display.clear()
        self.creatPillar()

    def creatPillar(self):
        list = [self.p1SafeY, self.p2SafeY, self.p3SafeY,self.p4SafeY,self.p5SafeY]
        pillarSafeY = random.choice(list)
        x = self.StartX

        for i in range(4):
            sleep(self.MOVETIME)
            display.clear()
            for y in range(5):
                if y == pillarSafeY: continue
                display.set_pixel(x,y,self.brightness)
            x = x - 1

p = Pillars()
p.Go()