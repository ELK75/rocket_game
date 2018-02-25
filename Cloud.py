
import random

class Cloud():

    def __init__(self):
        self.x = random.randint(10, 390)
        self.y = random.randint(0,600)
        self.change_x = 0
        self.change_y = 1
        
    def updateCloud(self, speed, height, width):
        self.y += self.change_y + (speed / 10)
        if (self.y >= height or self.x >= width or self.x <= 0):
            self.y = -10
            self.change_x = 0
            self.change_y = 1

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    