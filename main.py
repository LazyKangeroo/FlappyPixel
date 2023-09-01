from microbit import *
import random

class Play:
    MOVETIME = 400

    StartX = 4
    EndX = 0

    PLAYER = 9
    PILLAR = 3

    UP = 0
    DOWN = 1
    y = 1
    x = 1

    def __init__(self):
        pass

    def Go(self):
        self.list = [1,2,3]
        self.pillarX = self.StartX
        playing = True

        while playing:
            playing = self.colition()
            self.handelBtn()
            self.creatPillar()
        if playing == False:
            display.clear()
            display.scroll(f"Score : {self.sample}")

    def handelBtn(self):
        d = {}
        if button_a.is_pressed():
            d =  self.UP
        if button_b.is_pressed():
            d = self.DOWN

        if d == self.UP:
            self.y = self.y - 1
        if d == self.DOWN:
            self.y = self.y + 1

        if self.y < 0:
            self.y = 4
        elif self.y > 4:
            self.y = 0
        return

    def displayPillars(self):
        display.clear()

        for y in range(5):
            if y == self.pillarSafeY: continue
            display.set_pixel(self.pillarX,y,self.PILLAR)
            self.player()
        sleep(self.MOVETIME)

    def player(self):
        display.set_pixel(self.x,self.y,self.PLAYER)


    def creatPillar(self):
        if self.pillarX == self.StartX:
            self.pillarSafeY = random.choice(self.list)

        if self.pillarX == self.EndX:
            self.pillarX = self.StartX
            self.pillarSafeY = random.choice(self.list)

        self.displayPillars()

        if self.pillarX != self.EndX:
            self.pillarX = self.pillarX - 1
        return

    def colition(self):
        if self.pillarX == self.x and self.pillarSafeY != self.y:
            return False
        elif self.pillarX == self.x and self.pillarSafeY == self.y:
            self.sample = self.sample + 1
            return True
        else:
            return True

p = Play()
p.Go()