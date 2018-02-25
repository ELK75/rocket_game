
import random

class Meteor():

    def __init__(self):
        self.x = random.randint(100, 300)
        self.y = 1
        self.change_x = random.randint(-5, 5)
        self.change_y = 1
        
    def updateMeteor(self, speed, height, width, rocket, rocketValues):
        self.x += self.change_x
        self.y += self.change_y + ((speed * 10)/rocket.getMaxVelocity(rocketValues[3],rocketValues[0],rocketValues[2],rocketValues[1]))
        if (self.y >= height or self.x >= width or self.x <= 0):
            Meteor.__init__(self)

    def collision(self, rocket):
        if (rocket.getPos_x() <= self.x and self.x <= rocket.getPos_x() + rocket.getWidth() - 8
        and rocket.getPos_y() <= self.y and self.y <= rocket.getPos_y() + rocket.getLength()):
            return True
        return False

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    