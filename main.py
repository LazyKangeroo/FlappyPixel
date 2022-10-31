from microbit import *

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
            self.dirction = self.Down
            ButtonPressed = True

        elif button_b.is_pressed():
            while (button_b.is_pressed()):
                sleep(self.SAMPLETIME)
            self.dirction = self.Up
            ButtonPressed = True

        return ButtonPressed

    def move(self):
        if self.dirction == self.Up:
            y = y + 1
