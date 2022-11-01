from shutil import move
from microbit import *
import random

class Flappy:
    Non = 0
    Up = 1
    Down = 2

    PLAYERBRIGHT = 9
    PILLERSBRIGHT = 6
    SAMPLETIME = 50
    SAMPELERMOVE = 10

    def __init__(self):
        pass

    def startGame(self):
        display.clear()
        self.dirction = self.Non
        self.score = 0

        playing = True

        sample = 0
        while (playing):
            sleep(self.SAMPLETIME)
            ButtonPressed = self.handelBtn()
            sample = sample +1

            if ButtonPressed or sample == self.SAMPELERMOVE:
                playing = self.move()
                sample = 0

        display.scroll("Score = " + str(self.score), 100)
        display.clear()

    def handelBtn(self):
        ButtonPressed = False

        if button_a.is_pressed():
            while (button_a.is_pressed()):
                sleep(self.SAMPLETIME)
            self.down()
            ButtonPressed = True

        elif button_b.is_pressed():
            while (button_b.is_pressed()):
                sleep(self.SAMPLETIME)
            self.up()
            ButtonPressed = True

        return ButtonPressed

    def down(self):
        self.dirction = self.Down
        move()

    def up(self):
        self.dirction = self.Up
        move()

    def move(self):
        x = 1
        if self.dirction == self.Up:
            y = y -1
        if self.dirction == self.Down:
            y = y + 1

        display(x,y,self.PLAYERBRIGHT)
