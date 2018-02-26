
import random

class Cloud():

    def __init__(self):
        self.x = random.randint(10, 390)
        self.y = random.randint(-600, -40)
        self.change_x = 0
        self.change_y = 1
        
    def updateCloud(self, speed, height, width, rocket`):
        self.y += 2*(rocket.getHeight()**(1/3))
        if (self.y >= height or self.x >= width or self.x <= 0):
            self.y = -10
            self.change_x = 0
            self.change_y = 1

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    