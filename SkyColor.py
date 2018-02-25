
class SkyColor():

    def __init__(self, r=135, g=206, b=250):
        self.r = r
        self.g = g
        self.b = b
    
    def shift(self, h):
        if(h > 0):
            if(self.r > 0):
                self.r = (self.r - (h*self.r) / 100000)
            if(self.r > 0):
                self.g = (self.g - (self.g*h) / 100000)
            if(self.b > 0):
                self.b = (self.b - (self.b*h) / 100000)
        return (self.r, self.g, self.b)

    def resetSkyColor(self):
        self.r = 135
        self.g = 206
        self.b = 250
