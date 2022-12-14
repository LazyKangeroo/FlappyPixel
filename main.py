# Moverment
from microbit import *

class Move:
    Up = 0
    Down = 1

    y = 1
    x = 1
    brightness = 9

    display.clear()

    def __init__(self):
        pass

    def Go(self):
        #display.set_pixel(self.x,self.y,self.brightness)
        while True:
            self.direction = self.handelBtn()
            sleep(1000)
            display.clear()
            self.ChangePostion()
            display.set_pixel(self.x,self.y,self.brightness)

    def handelBtn(self):
        while not button_a.is_pressed() and not button_b.is_pressed():
            display.set_pixel(self.x,self.y,self.brightness)
        if button_a.is_pressed():
            return self.Up
        if button_b.is_pressed():
            return self.Down

    def ChangePostion(self):
        if self.direction == self.Up:
            self.y = self.y - 1
        if self.direction == self.Down:
            self.y = self.y + 1

        if self.y < 0:
            self.y = 4
        elif self.y > 4:
            self.y = 0
        return

move = Move()
move.Go()